import os
import re
from nicegui import ui
import json

#--------------------------------------------------
# Terminal nodes
#--------------------------------------------------

TERMINAL_NODES = [
    "query"
]

#--------------------------------------------------
# debug.jsonl helpers
#--------------------------------------------------

class SpanNode:
    def __init__(self, id, type, parent_id, start_timestamp, attrs=None):
        self.id = id
        self.type = type
        self.parent_id = parent_id
        self.start_timestamp = start_timestamp
        self.end_timestamp = None
        self.elapsed = None
        self.start_attrs = attrs or {}
        self.end_attrs = {}
        self.children = []

    def add_end_data(self, end_timestamp, elapsed, end_attrs=None):
        self.end_timestamp = end_timestamp
        self.elapsed = elapsed
        if end_attrs:
            # Merge end_attrs into attrs
            self.end_attrs.update(end_attrs)

    def add_child(self, child):
        self.children.append(child)

    def __str__(self, level=0):
        indent = "  " * level
        result = f"{indent}{self.type} ({self.id}):\n"
        result += f"{indent}  elapsed: {self.elapsed:.6f}s\n"

        if self.start_attrs or self.end_attrs:
            result += f"{indent}  start attributes:\n"
            for key, value in self.start_attrs.items():
                # Truncate long values for display
                if isinstance(value, str) and len(value) > 100:
                    value = value[:97] + "..."
                result += f"{indent}    {key}: {value}\n"
            result += f"{indent}  end attributes:\n"
            for key, value in self.end_attrs.items():
                # Truncate long values for display
                if isinstance(value, str) and len(value) > 100:
                    value = value[:97] + "..."
                result += f"{indent}    {key}: {value}\n"

        if self.children:
            result += f"{indent}  children:\n"
            for child in self.children:
                result += child.__str__(level + 2)

        return result

def parse_jsonl_to_tree(jsonl_content):
    lines = jsonl_content.strip().split('\n')
    nodes_by_id = {}
    root_nodes = []

    for line in lines:
        data = json.loads(line)
        event_type = data["event"]

        if event_type == "span_start":
            span = data["span"]
            node = SpanNode(
                id=span["id"],
                type=span["type"],
                parent_id=span["parent_id"],
                start_timestamp=span["start_timestamp"],
                attrs=span.get("attrs", {})
            )
            nodes_by_id[node.id] = node

            # Link to parent if exists
            if node.parent_id and node.parent_id in nodes_by_id:
                nodes_by_id[node.parent_id].add_child(node)
            elif node.parent_id is None:
                root_nodes.append(node)

        elif event_type == "span_end":
            node_id = data["id"]
            if node_id in nodes_by_id:
                nodes_by_id[node_id].add_end_data(
                    end_timestamp=data["end_timestamp"],
                    elapsed=data.get("elapsed", 0),
                    end_attrs=data.get("end_attrs", {})
                )

    return root_nodes

#--------------------------------------------------
# UI
#--------------------------------------------------

last_mod_time = None
current_json_objects = []
active_ix = None
active_item = None

def set_item(ix):
    global active_item, active_ix
    if active_ix != ix:
        active_ix = ix
        active_item = current_json_objects[ix]
        sidebar.refresh()
        details.refresh()

def format_time(t):
    if not t:
        return "..."
    if t > 1:
        return f"{t:.1f}s"
    elif t > 0.001:
        return f"{t*1000:.1f}ms"
    elif t > 0.0005:
        return f"{t*1000:.2f}ms"
    else:
        return f"{t*1000000:.0f}us"

def header(text):
    return ui.label(text).style("font-size: 1.3em; font-weight: bold;")

def replace_long_brace_contents(code_str):
    def replacement(match):
        string = match.group(0)
        if len(string) > 300:
            # Extract the first 50 and last 30 characters from the string within brackets
            return '{' + string[1:51] + '...' + string[-31:-1] + '}'
        else:
            # If the string is not longer than 300 characters, return it unchanged
            return string

    # This regex matches sequences of characters wrapped in { }
    brace_content_regex = r'\{[\s\S]*?\}'

    # Use the sub method to replace the matched strings with the result of the replacement function
    return re.sub(brace_content_regex, replacement, code_str)


def code(c, language="python"):
    c = replace_long_brace_contents(c)
    c = re.sub(r"→", "->", c)
    c = re.sub(r"⇑", "^", c)
    return ui.code(c, language=language).style("padding-right: 30px").classes("w-full")

@ui.refreshable
def details():
    if active_item:
        if active_item['event'] == "compilation":
            header(f"{active_item['source']['file']}: {active_item['source']['line']}")
            # with ui.row():
            code(active_item["source"]["block"] or active_item["emitted"])
            code(f"{active_item['emitted']}")
            header("IR")
            code(f"{active_item['task']}")
            header("Rewritten")
            code(f"{active_item['passes'][-1]['task']}")
            header("Passes")
            for p in active_item['passes']:
                with ui.column().classes("w-full"):
                    with ui.row():
                        ui.label(p['name'])
                        ui.label(f"({p['elapsed']*1000000:.0f} us)")
                    code(p['task'])
        elif active_item['event'] == "time":
            ui.label(f"{active_item['type']} | {format_time(active_item['elapsed'])} | {active_item['results']['count']}")
            vals = active_item['results']['values']
            if len(vals):
                keys = [k for k in vals[0].keys()]
                columns = [{'name': k, 'label': k, 'field': k, "align": "left"} for k in keys]
                ui.table(columns=columns, rows=vals)
            if "code" in active_item:
                header("Code")
                code(active_item["code"])
            # ui.label(f"{active_item['results']['values']}").style('white-space: pre;')

def handle_attributes(attrs):
    if attrs.get("file"):
        ui.label(f"{attrs['file']}: {attrs['line']}")
    if attrs.get("source"):
        code(attrs["source"])
    if attrs.get("txn_id"):
        ui.label(f"txn_id: {attrs['txn_id']}")
    if attrs.get("name"):
        ui.label(f"{attrs['name']}")
    if attrs.get("code"):
        code(attrs["code"])
    if attrs.get("dsl"):
        code(attrs["dsl"])
    if attrs.get("metamodel"):
        code(attrs["metamodel"])
    if attrs.get("rel"):
        code(attrs["rel"])
    if attrs.get("results"):
        vals = attrs['results']
        if len(vals):
            keys = [k for k in vals[0].keys()]
            columns = [{'name': k, 'label': k, 'field': k, "align": "left"} for k in keys]
            ui.table(columns=columns, rows=vals)

def handle_body(span: SpanNode):
    handle_attributes(span.start_attrs)
    if span.children:
        for child in span.children:
            span_ui(child)
    handle_attributes(span.end_attrs)

def span_ui(span: SpanNode):
    with ui.column().style("background:#33333399; padding:5px 10px; margin:5px; "):
        if span.children or span.start_attrs or span.end_attrs:
            with ui.expansion(f"{span.type}",
                            caption=f"{format_time(span.elapsed)}",
                            value=True).classes('w-full').style("padding:0; margin:0;"):
                handle_body(span)
        else:
            with ui.row().style("padding:0; margin:0;"):
                ui.label(f"{span.type}")
                ui.label(f"{format_time(span.elapsed)}").style("color:#999; margin:0;")
                handle_body(span)




@ui.refreshable
def sidebar():
    with ui.column():
        for root in current_json_objects:
            span_ui(root)



def poll():
    global last_mod_time, active_item
    global current_json_objects
    # Check the last modification time of the file
    try:
        mod_time = os.path.getmtime('debug.jsonl')
        if last_mod_time is None or mod_time > last_mod_time:
            last_mod_time = mod_time
            # File has changed, read and parse the new content
            with open('debug.jsonl', 'r') as file:
                content = file.read()
                if content:
                    new_tree = parse_jsonl_to_tree(content)
                    # Update the current JSON objects
                    current_json_objects = new_tree

                    if active_ix is not None and len(current_json_objects) > active_ix:
                        active_item = current_json_objects[active_ix]
                    # Refresh the UI with the new objects
                    sidebar.refresh()
                    details.refresh()
    except FileNotFoundError:
        pass

def main(host="0.0.0.0", port=8080):
    ui.dark_mode().enable()
    with ui.row():
        with ui.column() as c:
            c.style("cursor: pointer;")
            sidebar()
        with ui.column() as c:
            c.style("padding-left: 2em;")
            details()

    ui.timer(1, poll)
    ui.run(reload=False, host=host, port=port)

if __name__ in {"__main__", "__mp_main__"}:
    main()
