"""Methods to build SVG badges for the README using shields.io icons."""

import colorsys

from osa_tool.readmeai.config.settings import Settings
from osa_tool.readmeai.utils.file_handler import FileHandler
from osa_tool.readmeai.utils.file_resource import get_resource_path

_comment = "<!-- default option, no dependency badges. -->\n"
_package = "osa_tool.readmeai.generators"
_submodule = "svg"


def build_default_badges(
    config: Settings,
    full_name: str,
    host: str,
) -> str:
    """Build metadata badges using shields.io."""
    return config.md.shieldsio_icons.format(
        host=host,
        full_name=full_name,
        badge_color=config.md.badge_color,
        badge_style=config.md.badge_style,
    )


def build_badges_tech_stack(
    dependencies: list[str],
    icons: dict[str, str],
    style: str,
) -> str:
    """Build HTML badges for project dependencies."""
    badges = [
        icons[str(dependency).lower()]
        for dependency in dependencies
        if str(dependency).lower() in icons
    ]
    badges = sort_badges(badges)
    badges = [badge[0].format(style) for badge in badges]
    return format_badges(badges)


def format_badges(badges: list[str]) -> str:
    """Format SVG badge icons as HTML."""
    total = len(badges)
    if badges is None or total == 0:
        return ""

    badges_per_line = total if total < 9 else (total // 2) + (total % 2)

    lines = []
    for i in range(0, total, badges_per_line):
        line = "\n\t".join(
            [
                f'<img src="{badge}"'
                f'alt="{badge.split("/badge/")[1].split("-")[0]}">'
                for badge in badges[i: i + badges_per_line]
            ],
        )
        lines.append(
            f"{line}\n\t<br>" if i + badges_per_line < total else f"{line}\n",
        )

    return "\n\t".join(lines)


def hex_to_hls(hex_color: str) -> tuple[float, float, float]:
    """Converts a hex color to HLS."""
    hex_color = hex_color.lstrip("#")
    rgb = tuple(int(hex_color[i: i + 2], 16) for i in (0, 2, 4))
    return colorsys.rgb_to_hls(rgb[0] / 255, rgb[1] / 255, rgb[2] / 255)


def sort_badges(badges: list[str]) -> list[tuple[str, str]]:
    """Sorts badges by color and then by name."""
    badges = [(badge[0], str(badge[1])) for badge in badges]
    badges = list(set(badges))
    return sorted(
        badges,
        key=lambda b: (
            (*hex_to_hls(b[1]), b[0]) if b[1] else (float("inf"), 0, 0, "")
        ),
    )


def shieldsio_icons(
    conf: Settings,
    dependencies: list,
    full_name: str,
    git_host: str,
) -> tuple[str, str]:
    """Generates badges for the README using shields.io icons."""
    icons_path = get_resource_path(
        conf.files.shieldsio_icons,
        _package,
        _submodule,
    )
    icons_dict = FileHandler().read(icons_path)
    default_icons = build_default_badges(conf, full_name, git_host)

    badges_tech_stack = build_badges_tech_stack(
        dependencies,
        icons_dict,
        conf.md.badge_style,
    )
    badges_tech_stack = conf.md.badges_tech_stack.format(
        align=conf.md.align,
        badges_tech_stack=badges_tech_stack,
    )
    return default_icons, badges_tech_stack
