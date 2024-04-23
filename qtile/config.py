# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
# import re
# import socket
import subprocess
# from typing import List  # noqa: F401
from libqtile import layout, bar, widget, hook, qtile
from libqtile.config import Drag, Group, Key, Match, Screen, Click  # , Rule
from libqtile.command import lazy
# from libqtile.widget import Spacer
from libqtile.utils import guess_terminal
# import arcobattery

# mod4 or mod=super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')
terminal = guess_terminal()


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


keys = [

    # Most of our keybindings are in sxhkd file - except these

    # SUPER + LAUNCH

    Key([mod], "Return", lazy.spawn(terminal), desc="Launchterminal"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload config"),
    Key([mod, "control"], "e", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt"),
    Key([mod], "space", lazy.spawn("rofi -show drun")),

    # SUPER + FUNCTION KEYS

    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),


    # SUPER + SHIFT KEYS

    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),


    # QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "m", lazy.next_layout()),

    # CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),


    # RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


    # FLIP LAYOUT FOR MONADTALL/MONADWIDE
    # Key([mod, "shift"], "f", lazy.layout.flip()),

    # FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),

    # MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

    # TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),

    # CHANGE MONITOR
    Key([mod, "shift"], "space", lazy.next_screen(), desc='Next monitor'),

    # bar show
    Key([mod], "b", lazy.hide_show_bar(), desc="Hides the bar"),

    # C U S T O M

    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume 0 +5%"), desc='Volume Up'),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume 0 -5%"), desc='volume down'),
    Key([], "XF86AudioMute",
        lazy.spawn("pulsemixer --toggle-mute"), desc='Volume Mute'),
    Key([], "XF86AudioPlay",
        lazy.spawn("playerctl play-pause"), desc='playerctl'),
    Key([mod], "l",
        lazy.spawn("xset s activate"), desc='Lock screen'),
    # Key([], "XF86AudioPrev",
    #    lazy.spawn("playerctl previous"), desc='playerctl'),
    # Key([], "XF86AudioNext",`
    #     lazy.spawn("playerctl next"), desc='playerctl'),
    Key([], "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl s 10%+"), desc='brightness UP'),
    Key([], "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl s 10%-"), desc='brightness Down'),
    # Key([mod], "e",
    #    lazy.spawn("thunar"), desc='file manager'),
    Key([mod], "h",
        lazy.spawn("roficlip"), desc='clipboard'),
    Key([mod], "s",
        lazy.spawn("flameshot gui"), desc='Screenshot'),
]


def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen:
            qtile.cmd_to_screen(i - 1)


def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen:
            qtile.cmd_to_screen(i + 1)


keys.extend([
    # MOVE WINDOW TO NEXT SCREEN
    Key([mod, "shift"], "Right",
        lazy.function(window_to_next_screen, switch_screen=True)),
    Key([mod, "shift"], "Left",
        lazy.function(window_to_previous_screen, switch_screen=True)),
])

groups = []

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
# group_labels = ["", "", "", "", "", "", "", "", "", "",]

group_layouts = [
    "bsp",
    "bsp",
    "bsp",
    "bsp",
    "bsp",
    "bsp",
    "bsp",
    "bsp",
    "bsp",
    "bsp"
]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

        # CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift"], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW
        Key([mod, "shift"], i.name,
            lazy.window.togroup(i.name), lazy.group[i.name].toscreen()),
    ])


def init_layout_theme():
    return {"margin": 5,
            "border_width": 2,
            "border_focus": "#5e81ac",
            "border_normal": "#4c566a"
            }


layout_theme = init_layout_theme()

layouts = [
    layout.MonadTall(margin=8,
                     border_width=3,
                     border_focus="#5e81ac",
                     border_normal="#4c566a"
                     ),
    # layout.MonadTall(**layout_theme),
    layout.MonadWide(margin=8,
                     border_width=3,
                     border_focus="#5e81ac",
                     border_normal="#4c566a"
                     ),
    # layout.MonadWide(**layout_theme),
    # layout.Stack(num_stacks=2),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.Tile(**layout_theme),
    layout.Max(**layout_theme)
]


# COLORS FOR THE BAR
# Theme name : My Custom themening
def init_colors():
    return [["#2F343F", "#2F343F"],  # color 0
            ["#353446", "#353446"],  # color 1
            # ["#2F343F", "#2F343F"],
            ["#c0c5ce", "#c0c5ce"],  # color 2
            ["#fba922", "#fba922"],  # color 3
            ["#3384d0", "#3384d0"],  # color 4
            ["#f3f4f5", "#f3f4f5"],  # color 5
            ["#cd1f3f", "#cd1f3f"],  # color 6
            ["#62FF00", "#62FF00"],  # color 7
            ["#6790eb", "#6790eb"],  # color 8
            ["#a9a9a9", "#a9a9a9"]]  # color 9


colors = init_colors()


def search():
    qtile.cmd_spawn("rofi -show drun")


def power():
    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/power")


# WIDGETS FOR THE BAR

def init_widgets_defaults():
    return dict(font="Noto Sans",
                fontsize=8,
                padding=2,
                background=colors[1])


widget_defaults = init_widgets_defaults()


def init_widgets_list():
    # prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
        widget.Spacer(
            length=4,
            background=colors[1],
            ),


        # widget.Image(
        #    filename='~/.config/qtile/Assets/launch_Icon.png',
        #    margin=2,
        #    background=colors[1],
        #    mouse_callbacks={"Button1":power},
        # ),

        # widget.Image(
        #    filename='~/.config/qtile/Assets/6.png',
        # ),


        widget.GroupBox(
            fontsize=24,
            borderwidth=3,
            highlight_method='block',
            active='#CAA9E0',
            block_highlight_text_color="#91B1F0",
            highlight_color='#4B427E',
            inactive='#282738',
            foreground='#4B427E',
            background=colors[1],
            this_current_screen_border='#353446',
            this_screen_border='#353446',
            other_current_screen_border='#353446',
            other_screen_border='#353446',
            urgent_border='#353446',
            rounded=True,
            disable_drag=True,
         ),


        widget.Spacer(
            length=8,
            background=colors[1],
        ),


        widget.Image(
            filename='~/.config/qtile/Assets/1.png',
        ),


        widget.Image(
            filename='~/.config/qtile/Assets/layout.png',
            background="#353446"
        ),


        widget.CurrentLayout(
            background=colors[1],
            foreground=colors[5],
            fmt='{}',
            font="JetBrains Mono Bold",
            fontsize=13,
        ),


        widget.Image(
            filename='~/.config/qtile/Assets/5.png',
        ),


        widget.Image(
            filename='~/.config/qtile/Assets/search.png',
            margin=2,
            background=colors[1],
            mouse_callbacks={"Button1": search},
        ),

        widget.TextBox(
            fmt='Search',
            background=colors[1],
            font="JetBrains Mono Bold",
            fontsize=13,
            foreground=colors[5],
            mouse_callbacks={"Button1": search},
        ),

        widget.Spacer(
            length=8,
            background=colors[1],
        ),

        widget.Image(
            filename='~/.config/qtile/Assets/4.png',
        ),


        widget.WindowName(
            background=colors[1],
            format="{name}",
            font='JetBrains Mono Bold',
            foreground=colors[5],
            empty_group_string='Desktop',
            fontsize=13,

        ),

        widget.Image(
            filename='~/.config/qtile/Assets/3.png',
        ),


        widget.Systray(
            background=colors[1],
            fontsize=2,
        ),


        widget.TextBox(
            text=' ',
            background=colors[1],
        ),


        widget.Image(
            filename='~/.config/qtile/Assets/6.png',
            background=colors[1],
        ),


        widget.Image(
            filename='~/.config/qtile/Assets/Drop1.png',
        ),


        # widget.Net(
        #     format=' {up}   {down} ',
        #     background=colors[1],
        #     foreground=colors[5],
        #     font="JetBrains Mono Bold",
        #     prefix='k',
        # ),
        # widget.Image(
        #    filename='~/.config/qtile/Assets/2.png',
        # ),

        # widget.Spacer(
        #     length=8,
        #     background=colors[1],
        # ),
        widget.Image(
            filename='~/.config/qtile/Assets/Misc/thermo.png',
            background=colors[1],
        ),


        widget.Spacer(
            length=-7,
            background=colors[1],
        ),


        widget.ThermalSensor(
            foreground=colors[5],
            foreground_alert=colors[6],
            background=colors[1],
            font="JetBrains Mono Bold",
            metric=True,
            padding=3,
            threshold=80
        ),
        widget.Image(
            filename='~/.config/qtile/Assets/2.png',
        ),


        widget.Spacer(
            length=8,
            background=colors[1],
        ),


        widget.Image(
            filename='~/.config/qtile/Assets/Misc/ram.png',
            background=colors[1],
        ),


        widget.Spacer(
            length=-7,
            background=colors[1],
        ),


        widget.Memory(
            background=colors[1],
            format='{MemUsed: .0f}{mm}',
            foreground=colors[5],
            font="JetBrains Mono Bold",
            fontsize=13,
            update_interval=5,
        ),


        # widget.Image(
        # filename='~/.config/qtile/Assets/Drop2.png',
        # ),



        widget.Image(
            filename='~/.config/qtile/Assets/2.png',
        ),


        widget.Spacer(
            length=8,
            background=colors[1],
        ),


        widget.BatteryIcon(
            theme_path='~/.config/qtile/Assets/Battery/',
            background=colors[1],
            scale=1,
        ),


        widget.Battery(
            font='JetBrains Mono Bold',
            background=colors[1],
            foreground=colors[5],
            format='{percent:2.0%}',
            fontsize=13,
        ),


        widget.Image(
            filename='~/.config/qtile/Assets/2.png',
        ),


        widget.Spacer(
            length=8,
            background=colors[1],
        ),


        # widget.Battery(
        #     format=' {percent:2.0%}',
        #     font="JetBrains Mono ExtraBold",
        #     fontsize=12,
        #     padding=10,
        #     background=colors[1],
        # ),

        # widget.Memory(
        #     format='﬙{MemUsed: .0f}{mm}',
        #     font="JetBrains Mono Bold",
        #     fontsize=12,
        #     padding=10,
        #     background='#4B4D66',
        # ),

        widget.Volume(
            font='JetBrainsMono Nerd Font',
            theme_path='~/.config/qtile/Assets/Volume/',
            emoji=True,
            fontsize=13,
            background=colors[1],
        ),


        widget.Spacer(
            length=-5,
            background=colors[1],
        ),


        widget.Volume(
            font='JetBrains Mono Bold',
            background=colors[1],
            foreground=colors[5],
            fontsize=13,
        ),


        widget.Image(
            filename='~/.config/qtile/Assets/5.png',
            background=colors[1],
        ),


        widget.Image(
            filename='~/.config/qtile/Assets/Misc/clock.png',
            background=colors[1],
            margin_y=6,
            margin_x=5,
        ),


        widget.Clock(
            format="%H:%M %d-%m-%Y",
            background=colors[1],
            foreground=colors[5],
            font="JetBrains Mono Bold",
            fontsize=13,
        ),


        widget.Spacer(
            length=18,
            background=colors[1],
        ),
    ]
    # widgets_list_legacy = [
    #             widget.GroupBox(
    #                     font="sans",
    #                     fontsize=16,
    #                     margin_y=3,
    #                     margin_x=0,
    #                     padding_y=6,
    #                     padding_x=5,
    #                     borderwidth=0,
    #                     disable_drag=True,
    #                     active=colors[9],
    #                     inactive=colors[5],
    #                     rounded=False,
    #                     highlight_method="text",
    #                     this_current_screen_border=colors[8],
    #                     foreground=colors[2],
    #                     background=colors[1]
    #                     ),
    #             widget.Sep(
    #                     linewidth=1,
    #                     padding=10,
    #                     foreground=colors[2],
    #                     background=colors[1]
    #                     ),
    #             widget.CurrentLayout(
    #                     font="Noto Sans Bold",
    #                     foreground=colors[5],
    #                     background=colors[1]
    #                     ),
    #             widget.Sep(
    #                     linewidth=1,
    #                     padding=10,
    #                     foreground=colors[2],
    #                     background=colors[1]
    #                     ),
    #             widget.WindowName(font="Noto Sans",
    #                     fontsize=12,
    #                     foreground=colors[5],
    #                     background=colors[1],
    #                     ),
    #             widget.Net(
    #                      font="Noto Sans",
    #                      fontsize=12,
    #                      interface="enp0s31f6",
    #                      foreground=colors[2],
    #                      background=colors[1],
    #                      padding=0,
    #                      ),
    #             widget.Sep(
    #                      linewidth=1,
    #                      padding=10,
    #                      foreground=colors[2],
    #                      background=colors[1]
    #                      ),
    #            # widget.NetGraph(
    #            #          font="Noto Sans",
    #            #          fontsize=12,
    #            #          bandwidth="down",
    #            #          interface="auto",
    #            #          fill_color=colors[8],
    #            #          foreground=colors[2],
    #            #          background=colors[1],
    #            #          graph_color=colors[8],
    #            #          border_color=colors[2],
    #            #          padding=0,
    #            #          border_width=1,
    #            #          line_width=1,
    #            #          ),
    #            # widget.Sep(
    #            #          linewidth=1,
    #            #          padding=10,
    #            #          foreground=colors[2],
    #            #          background=colors[1]
    #            #          ),
    #            # # do not activate in Virtualbox - will break qtile
    #             widget.ThermalSensor(
    #                      foreground=colors[5],
    #                      foreground_alert=colors[6],
    #                      background=colors[1],
    #                      metric=True,
    #                      padding=3,
    #                      threshold=80
    #                      ),
    #             # # battery option 2  from Qtile
    #             widget.Sep(
    #                      linewidth=1,
    #                      padding=10,
    #                      foreground=colors[2],
    #                      background=colors[1]
    #                      ),
    #             widget.Battery(
    #                      font="Noto Sans",
    #                      update_interval=10,
    #                      fontsize=12,
    #                      foreground=colors[5],
    #                      background=colors[1],
    #                      ),
    #             widget.Sep(
    #                      linewidth=1,
    #                      padding=10,
    #                      foreground=colors[2],
    #                      background=colors[1]
    #                      ),
    #             widget.TextBox(
    #                      font="FontAwesome",
    #                      text="  ",
    #                      foreground=colors[6],
    #                      background=colors[1],
    #                      padding=0,
    #                      fontsize=16
    #                      ),
    #             widget.CPUGraph(
    #                      border_color=colors[2],
    #                      fill_color=colors[8],
    #                      graph_color=colors[8],
    #                      background=colors[1],
    #                      border_width=1,
    #                      line_width=1,
    #                      core="all",
    #                      type="box"
    #                      ),
    #             widget.Sep(
    #                      linewidth=1,
    #                      padding=10,
    #                      foreground=colors[2],
    #                      background=colors[1]
    #                      ),
    #             widget.TextBox(
    #                      font="FontAwesome",
    #                      text="  ",
    #                      foreground=colors[4],
    #                      background=colors[1],
    #                      padding=0,
    #                      fontsize=16
    #                      ),
    #             widget.Memory(
    #                      font="Noto Sans",
    #                      # format='{MemUsed}M/{MemTotal}M',
    #                      # update_interval=1,
    #                      fontsize=12,
    #                      foreground=colors[5],
    #                      background=colors[1],
    #                     ),
    #             widget.Sep(
    #                      linewidth=1,
    #                      padding=10,
    #                      foreground=colors[2],
    #                      background=colors[1]
    #                      ),
    #            widget.TextBox(
    #                     font="FontAwesome",
    #                     text="  ",
    #                     foreground=colors[3],
    #                     background=colors[1],
    #                     padding=0,
    #                     fontsize=16
    #                     ),
    #            widget.Clock(
    #                     foreground=colors[5],
    #                     background=colors[1],
    #                     fontsize=12,
    #                     format="%Y-%m-%d %H:%M"
    #                     ),
    #             widget.Sep(
    #                      linewidth=1,
    #                      padding=10,
    #                      foreground=colors[2],
    #                      background=colors[1]
    #                      ),
    #            widget.Systray(
    #                     background=colors[1],
    #                     icon_size=20,
    #                     padding=4
    #                     ),
    #           ]
    return widgets_list


widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2


widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [Screen(top=bar.Bar(
                widgets=init_widgets_screen1(),
                size=30,
                opacity=0.8,
                border_color='#282738',
                border_width=[1, 1, 1, 1],
                margin=[15, 15, 6, 15]
                )),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(),
                               size=30,
                               opacity=0.8,
                               border_color='#282738',
                               border_width=[1, 1, 1, 1],
                               margin=[15, 15, 6, 15]
                               ))
            ]


screens = init_screens()

# screens = [
#
#     Screen(
#         top=bar.Bar(
#             30,
#             border_color = '#282738',
#             border_width = [0,0,0,0],
#             margin = [15,15,6,15],
#
#         ),
#     ),
# ]

# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1",
         lazy.window.set_position_floating(),
         start=lazy.window.get_position()),

    Drag([mod], "Button3",
         lazy.window.set_size_floating(),
         start=lazy.window.get_size()),

    Click([mod], "Button2",
          lazy.window.bring_to_front())
]
dgroups_key_binder = None
dgroups_app_rules = []

# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
# BEGIN

# ########################################################
# ############### assgin apps to groups ##################
# ########################################################
# @hook.subscribe.client_new
# def assign_app_group(client):
#     d={}
#     ###############################################################################
#     Us xprop fo find the value of WM_CLASS(STRING)->First field is sufficient
#     ###############################################################################
#     d[group_names[0]]=["Navigator", "Firefox", "Vialdi-stable",
#           "Vivaldi-snapshot", "Chromium",
#               "Google-chrome", "Brave", "Brave-browser",
#               "navigator", "firefox", "vivaldi-stable", "vivaldi-snapshot",
#               "chromium", "google-chrome", "brave", "brave-browser", ]
#     d[group_names[1]]=[ "Atom", "Subl", "Geany", "Brackets", "Code-oss",
#               "Code", "TelegramDesktop", "Discord",
#                "atom", "subl", "geany", "brackets",
#               "code-oss", "code", "telegramDesktop", "discord", ]
#     d[group_names[2]]=["Inkscape", "Nomacs", "Ristretto", "Nitrogen", "Feh",
#               "inkscape", "nomacs", "ristretto", "nitrogen", "feh", ]
#     d[group_names[3]]=["Gimp", "gimp" ]
#     d[group_names[4]]=["Meld", "meld", "org.gnome.meld" "org.gnome.Meld" ]
#     d[group_names[5]]=["Vlc","vlc", "Mpv", "mpv" ]
#     d[group_names[6]]=["VirtualBox Manager", "VirtualBox Machine",
#           "Vmplayer", "virtualbox manager", "virtualbox machine", "vmplayer",
#           ]
#     d[group_names[7]]=["Thunar", "Nemo", "Caja", "Nautilus",
#           "org.gnome.Nautilus", "Pcmanfm", "Pcmanfm-qt",
#           "thunar", "nemo", "caja", "nautilus",
#           "org.gnome.nautilus", "pcmanfm", "pcmanfm-qt", ]
#     d[group_names[8]]=["Evolution", "Geary", "Mail", "Thunderbird",
#               "evolution", "geary", "mail", "thunderbird" ]
#     d[group_names[9]]=["Spotify", "Pragha", "Clementine", "Deadbeef",
#           "Audacious", "spotify", "pragha",
#           "clementine", "deadbeef", "audacious" ]
#     ######################################################################################
#
# wm_class=client.window.get_wm_class()[0]
#
#     for i in range(len(d)):
#         if wm_class in list(d.values())[i]:
#             group=list(d.keys())[i]
#             client.togroup(group)
#             client.group.cmd_toscreen(toggle=False)

# END
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME


main = None


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])


@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True


floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='Arandr'),
    Match(wm_class='feh'),
    Match(wm_class='Galculator'),
    Match(wm_class='archlinux-logout'),
    Match(wm_class='xfce4-terminal'),

],  fullscreen_border_width=0, border_width=0)
auto_fullscreen = True

focus_on_window_activation = "focus"  # or smart

wmname = "LG3D"
