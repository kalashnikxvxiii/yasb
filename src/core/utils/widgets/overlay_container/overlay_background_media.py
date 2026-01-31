"""
Background media handler for Overlay Container Widget.
No OpenGL/shaders; optional placeholder for future media background (e.g. cava layer).
"""

from __future__ import annotations


class OverlayBackgroundMedia:
    """Placeholder for media background (e.g. cava). get_widget() returns None; no background layer."""

    def __init__(self, media_config: dict, parent_widget) -> None:
        self.config = media_config
        self.parent = parent_widget
        self.widget = None
        # Optional: when enabled, could instantiate a widget by name from config (e.g. cava)
        # For now we do not add a background layer; overlay shows only the child widget.

    def get_widget(self):
        """Return the media widget or None."""
        return self.widget

    def cleanup(self) -> None:
        """No-op; no resources to release."""
        if self.widget:
            try:
                self.widget.setParent(None)
                self.widget.deleteLater()
            except (RuntimeError, AttributeError):
                pass
            self.widget = None
