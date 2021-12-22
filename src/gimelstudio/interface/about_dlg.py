# ----------------------------------------------------------------------------
# Gimel Studio Copyright 2019-2021 by Noah Rahm and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------

import wx

from gswidgetkit import Label, Button

import gimelstudio.constants as const 
from gimelstudio.datafiles import ICON_GIMELSTUDIO_ICO, ICON_LICENSE
from gimelstudio.datafiles.icons import (ICON_CREDITS, ICON_DISCORD, ICON_GITHUB, 
                                         ICON_WEBSITE, ICON_YOUTUBE)


class AboutDialog(wx.Dialog):
    def __init__(self, parent, title):
        wx.Dialog.__init__(self, parent, title=title, size=(500, 600))
        self.SetBackgroundColour(const.DARK_COLOR)

        self.parent = parent

        self.BuildUI()
        self.Center()

    def BuildUI(self):
        panel = wx.Panel(self)
        panel.SetBackgroundColour(const.DARK_COLOR)

        info_panel = wx.Panel(panel)
        info_panel.SetBackgroundColour(const.DARK_COLOR)

        info_sizer = wx.BoxSizer(wx.VERTICAL)

        app_name_lbl = Label(info_panel, label=const.APP_NAME, font_bold=True)
        app_name_lbl.SetFont(app_name_lbl.GetFont().Scale(2))
        info_sizer.Add(app_name_lbl, 0, flag=wx.LEFT|wx.EXPAND, border=8)

        app_version_lbl = Label(info_panel, label=const.APP_VERSION_FULL, font_bold=True)
        app_version_lbl.SetFont(app_version_lbl.GetFont())
        info_sizer.Add(app_version_lbl, 0, flag=wx.EXPAND|wx.LEFT, border=8)

        app_desc_lbl = Label(info_panel, label=const.APP_COPYRIGHT)
        app_desc_lbl.SetFont(app_desc_lbl.GetFont().Smaller())
        info_sizer.Add(app_desc_lbl, 0, flag=wx.LEFT|wx.TOP, border=8)

        info_panel.SetSizer(info_sizer)

        sizer = wx.GridBagSizer(1, 1)

        logo_bmp = wx.Image.ConvertToBitmap(ICON_GIMELSTUDIO_ICO.GetImage().Scale(85, 85))
        icon = wx.StaticBitmap(panel, bitmap=logo_bmp)
        sizer.Add(icon, pos=(0, 1), flag=wx.TOP|wx.LEFT|wx.ALIGN_LEFT, border=10)

        sizer.Add(info_panel, pos=(0, 2), flag=wx.TOP|wx.RIGHT|wx.LEFT|wx.BOTTOM, border=10)

        # Add buttons
        website_btn = Button(panel, label="Official website",
                             bmp=(ICON_WEBSITE.GetBitmap(), 'left'))
        sizer.Add(website_btn, pos=(3, 2), span=(1, 3), flag=wx.TOP|wx.RIGHT|wx.EXPAND, border=8)

        github_btn = Button(panel, label="Github repo",
                             bmp=(ICON_GITHUB.GetBitmap(), 'left'))
        sizer.Add(github_btn, pos=(4, 2), span=(1, 3), flag=wx.TOP|wx.RIGHT|wx.EXPAND, border=8)

        license_btn = Button(panel, label="Apache-2.0 License",
                             bmp=(ICON_LICENSE.GetBitmap(), 'left'))
        sizer.Add(license_btn, pos=(5, 2), span=(1, 3), flag=wx.TOP|wx.RIGHT|wx.EXPAND, border=8)

        credits_btn = Button(panel, label="Contributors",
                             bmp=(ICON_CREDITS.GetBitmap(), 'left'))
        sizer.Add(credits_btn, pos=(6, 2), span=(1, 3), flag=wx.TOP|wx.RIGHT|wx.EXPAND, border=8)

        discord_btn = Button(panel, label="Discord chat",
                             bmp=(ICON_DISCORD.GetBitmap(), 'left'))
        sizer.Add(discord_btn, pos=(8, 2), span=(1, 3), flag=wx.TOP|wx.RIGHT|wx.EXPAND, border=8)

        youtube_btn = Button(panel, label="Youtube channel",
                             bmp=(ICON_YOUTUBE.GetBitmap(), 'left'))
        sizer.Add(youtube_btn, pos=(9, 2), span=(1, 3), flag=wx.TOP|wx.RIGHT|wx.EXPAND, border=8)

        # Add spacing
        sizer.Add((10, 10), pos=(10, 0))
        sizer.Add((10, 10), pos=(10, 5))

        panel.SetSizer(sizer)
        sizer.Fit(self)
 