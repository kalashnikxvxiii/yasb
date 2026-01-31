from typing import Any

DEFAULTS: dict[str, Any] = {
    "target": "full",
    "target_widget": "",
    "position": "behind",
    "offset_x": 0,
    "offset_y": 0,
    "width": "auto",
    "height": "auto",
    "opacity": 1.0,
    "pass_through_clicks": True,
    "z_index": 0,
    "child_widget_name": "",
    "show_toggle": True,
    "toggle_label": "",
    "auto_show": True,
    "callbacks": {"on_left": "toggle_overlay", "on_middle": "do_nothing", "on_right": "do_nothing"},
    "container_padding": {"top": 0, "left": 0, "bottom": 0, "right": 0},
    "container_shadow": {"enabled": False, "color": "black", "offset": [1, 1], "radius": 3},
    "label_shadow": {"enabled": False, "color": "black", "offset": [1, 1], "radius": 3},
    "background_media": {"enabled": False},
    "background_shader": {"enabled": False, "preset": "plasma", "speed": 1.0, "scale": 1.0, "opacity": 1.0, "colors": []},
}

VALIDATION_SCHEMA: dict[str, Any] = {
    "target": {"type": "string", "default": DEFAULTS["target"]},
    "target_widget": {"type": "string", "default": DEFAULTS["target_widget"]},
    "position": {"type": "string", "default": DEFAULTS["position"]},
    "offset_x": {"type": "integer", "default": DEFAULTS["offset_x"]},
    "offset_y": {"type": "integer", "default": DEFAULTS["offset_y"]},
    "width": {"type": ["string", "integer"], "default": DEFAULTS["width"]},
    "height": {"type": ["string", "integer"], "default": DEFAULTS["height"]},
    "opacity": {"type": "float", "default": DEFAULTS["opacity"]},
    "pass_through_clicks": {"type": "boolean", "default": DEFAULTS["pass_through_clicks"]},
    "z_index": {"type": "integer", "default": DEFAULTS["z_index"]},
    "child_widget_name": {"type": "string", "default": DEFAULTS["child_widget_name"]},
    "show_toggle": {"type": "boolean", "default": DEFAULTS["show_toggle"]},
    "toggle_label": {"type": "string", "default": DEFAULTS["toggle_label"]},
    "auto_show": {"type": "boolean", "default": DEFAULTS["auto_show"]},
    "callbacks": {
        "type": "dict",
        "schema": {
            "on_left": {"type": "string", "default": DEFAULTS["callbacks"]["on_left"]},
            "on_middle": {"type": "string", "default": DEFAULTS["callbacks"]["on_middle"]},
            "on_right": {"type": "string", "default": DEFAULTS["callbacks"]["on_right"]},
        },
        "default": DEFAULTS["callbacks"],
    },
    "container_padding": {
        "type": "dict",
        "schema": {
            "top": {"type": "integer", "default": DEFAULTS["container_padding"]["top"]},
            "left": {"type": "integer", "default": DEFAULTS["container_padding"]["left"]},
            "bottom": {"type": "integer", "default": DEFAULTS["container_padding"]["bottom"]},
            "right": {"type": "integer", "default": DEFAULTS["container_padding"]["right"]},
        },
        "default": DEFAULTS["container_padding"],
    },
    "container_shadow": {
        "type": "dict",
        "schema": {
            "enabled": {"type": "boolean", "default": DEFAULTS["container_shadow"]["enabled"]},
            "color": {"type": "string", "default": DEFAULTS["container_shadow"]["color"]},
            "offset": {"type": "list", "default": DEFAULTS["container_shadow"]["offset"]},
            "radius": {"type": "integer", "default": DEFAULTS["container_shadow"]["radius"]},
        },
        "default": DEFAULTS["container_shadow"],
    },
    "label_shadow": {
        "type": "dict",
        "schema": {
            "enabled": {"type": "boolean", "default": DEFAULTS["label_shadow"]["enabled"]},
            "color": {"type": "string", "default": DEFAULTS["label_shadow"]["color"]},
            "offset": {"type": "list", "default": DEFAULTS["label_shadow"]["offset"]},
            "radius": {"type": "integer", "default": DEFAULTS["label_shadow"]["radius"]},
        },
        "default": DEFAULTS["label_shadow"],
    },
    "background_media": {
        "type": "dict",
        "schema": {
            "enabled": {"type": "boolean", "default": DEFAULTS["background_media"]["enabled"]},
        },
        "default": DEFAULTS["background_media"],
    },
    "background_shader": {
        "type": "dict",
        "schema": {
            "enabled": {"type": "boolean", "default": DEFAULTS["background_shader"]["enabled"]},
            "preset": {"type": "string", "default": DEFAULTS["background_shader"]["preset"]},
            "speed": {"type": "float", "default": DEFAULTS["background_shader"]["speed"]},
            "scale": {"type": "float", "default": DEFAULTS["background_shader"]["scale"]},
            "opacity": {"type": "float", "default": DEFAULTS["background_shader"]["opacity"]},
            "colors": {"type": "list", "default": DEFAULTS["background_shader"]["colors"]},
        },
        "default": DEFAULTS["background_shader"],
    },
}
