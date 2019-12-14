#!/usr/bin/python
# -*- coding: utf-8 -*-
#  Copyright (C) 2017-2019 Sascha Montellese <montellese@kodi.tv>
#
#  SPDX-License-Identifier: GPL-2.0-or-later
#  See LICENSES/README.md for more information.
#

import xbmcmediaimport

# import related constants
SUPPORTED_MEDIA_TYPES = set([ xbmcmediaimport.MediaTypeMovie, xbmcmediaimport.MediaTypeMusicVideo,
    xbmcmediaimport.MediaTypeTvShow, xbmcmediaimport.MediaTypeSeason, xbmcmediaimport.MediaTypeEpisode ])

# API related constants
EMBY_PROTOCOL = 'emby'
EMBY_API_KEY_HEADER = 'X-MediaBrowser-Token'
EMBY_AUTHORIZATION_HEADER = 'X-Emby-Authorization'
EMBY_ACCEPT_ENCODING = 'application/json'
EMBY_CONTENT_TYPE = EMBY_ACCEPT_ENCODING

URL_USERS = 'Users'
URL_USERS_PUBLIC = 'Public'
URL_VIEWS = 'Views'
URL_ITEMS = 'Items'
URL_VIDEOS = 'Videos'
URL_PLAYING_ITEMS = 'PlayingItems'
URL_PLAYED_ITEMS = 'PlayedItems'
URL_SESSIONS = 'Sessions'
URL_SESSIONS_PLAYING = 'Playing'
URL_SESSIONS_PLAYING_PROGRESS = 'Progress'
URL_SESSIONS_PLAYING_STOPPED = 'Stopped'
URL_USER_DATA = 'UserData'
URL_IMAGES = 'Images'
URL_AUTHENTICATE = 'Authenticate'
URL_AUTHENTICATE_BY_NAME = 'AuthenticateByName'
URL_SYSTEM = 'System'
URL_SYSTEM_INFO = 'Info'
URL_SYSTEM_INFO_PUBLIC = 'Public'

WS_MESSAGE_TYPE = 'MessageType'
WS_DATA = 'Data'
WS_MESSAGE_TYPE_LIBRARY_CHANGED = 'LibraryChanged'
WS_MESSAGE_TYPE_USER_DATA_CHANGED = 'UserDataChanged'
WS_LIBRARY_CHANGED_ITEMS_ADDED = 'ItemsAdded'
WS_LIBRARY_CHANGED_ITEMS_UPDATED = 'ItemsUpdated'
WS_LIBRARY_CHANGED_ITEMS_REMOVED = 'ItemsRemoved'
WS_USER_DATA_CHANGED_USER_DATA_LIST = 'UserDataList'
WS_USER_DATA_CHANGED_USER_DATA_ITEM_ID = 'ItemId'


PROPERTY_SYSTEM_INFO_ID = 'Id'
PROPERTY_SYSTEM_INFO_SERVER_NAME = 'ServerName'
PROPERTY_SYSTEM_INFO_VERSION = 'Version'

PROPERTY_VIEW_ID = 'Id'
PROPERTY_VIEW_NAME = 'Name'
PROPERTY_VIEW_COLLECTION_TYPE = 'CollectionType'

PROPERTY_ITEM_TOTAL_RECORD_COUNT = 'TotalRecordCount'
PROPERTY_ITEM_ITEMS = 'Items'
PROPERTY_ITEM_MEDIA_TYPE = 'MediaType'
PROPERTY_ITEM_TYPE = 'Type'
PROPERTY_ITEM_ID = 'Id'
PROPERTY_ITEM_IS_FOLDER = 'IsFolder'
PROPERTY_ITEM_CONTAINER = 'Container'
PROPERTY_ITEM_NAME = 'Name'
PROPERTY_ITEM_PREMIERE_DATE = 'PremiereDate'
PROPERTY_ITEM_PRODUCTION_YEAR = 'ProductionYear'
PROPERTY_ITEM_PATH = 'Path'
PROPERTY_ITEM_SORT_NAME = 'SortName'
PROPERTY_ITEM_ORIGINAL_TITLE = 'OriginalTitle'
PROPERTY_ITEM_DATE_CREATED = 'DateCreated'
PROPERTY_ITEM_COMMUNITY_RATING = 'CommunityRating'
PROPERTY_ITEM_VOTE_COUNT = 'VoteCount'
PROPERTY_ITEM_OFFICIAL_RATING = 'OfficialRating'
PROPERTY_ITEM_RUN_TIME_TICKS = 'RunTimeTicks'
PROPERTY_ITEM_USER_DATA = 'UserData'
PROPERTY_ITEM_USER_DATA_PLAYBACK_POSITION_TICKS = 'PlaybackPositionTicks'
PROPERTY_ITEM_USER_DATA_PLAY_COUNT = 'PlayCount'
PROPERTY_ITEM_USER_DATA_LAST_PLAYED_DATE = 'LastPlayedDate'
PROPERTY_ITEM_USER_DATA_PLAYED = 'Played'
PROPERTY_ITEM_OVERVIEW = 'Overview'
PROPERTY_ITEM_SHORT_OVERVIEW = 'ShortOverview'
PROPERTY_ITEM_TAGLINES = 'Taglines'
PROPERTY_ITEM_GENRES = 'Genres'
PROPERTY_ITEM_STUDIOS = 'Studios'
PROPERTY_ITEM_PRODUCTION_LOCATIONS = 'ProductionLocations'
PROPERTY_ITEM_PROVIDER_IDS = 'ProviderIds'
PROPERTY_ITEM_TAGS = 'Tags'
PROPERTY_ITEM_PEOPLE = 'People'
PROPERTY_ITEM_PEOPLE_NAME = 'Name'
PROPERTY_ITEM_PEOPLE_TYPE = 'Type'
PROPERTY_ITEM_PEOPLE_TYPE_ACTOR = 'Actor'
PROPERTY_ITEM_PEOPLE_TYPE_WRITER = 'Writer'
PROPERTY_ITEM_PEOPLE_TYPE_DIRECTOR = 'Director'
PROPERTY_ITEM_PEOPLE_ROLE = 'Role'
PROPERTY_ITEM_ROLE = 'Role'
PROPERTY_ITEM_INDEX_NUMBER = 'IndexNumber'
PROPERTY_ITEM_PARENT_INDEX_NUMBER = 'ParentIndexNumber'
PROPERTY_ITEM_SERIES_NAME = 'SeriesName'
PROPERTY_ITEM_STATUS = 'Status'
PROPERTY_ITEM_ARTISTS = 'Artists'
PROPERTY_ITEM_ALBUM = 'Album'
PROPERTY_ITEM_IMAGE_TAGS = 'ImageTags'
PROPERTY_ITEM_IMAGE_TAGS_PRIMARY = 'Primary'
PROPERTY_ITEM_IMAGE_TAGS_LOGO = 'Logo'
PROPERTY_ITEM_BACKDROP_IMAGE_TAGS = 'BackdropImageTags'
PROPERTY_ITEM_MEDIA_STREAMS = 'MediaStreams'
PROPERTY_ITEM_MEDIA_STREAM_TYPE = 'Type'
PROPERTY_ITEM_MEDIA_STREAM_CODEC = 'Codec'
PROPERTY_ITEM_MEDIA_STREAM_LANGUAGE = 'Language'
PROPERTY_ITEM_MEDIA_STREAM_HEIGHT = 'Height'
PROPERTY_ITEM_MEDIA_STREAM_WIDTH = 'Width'
PROPERTY_ITEM_MEDIA_STREAM_CHANNELS = 'Channels'

PROPERTY_USER_NAME = 'Name'
PROPERTY_USER_ID = 'Id'
PROPERTY_USER_POLICY = 'Policy'
PROPERTY_USER_IS_DISABLED = 'IsDisabled'

PROPERTY_USER_AUTHENTICATION_USERNAME = 'Username'
PROPERTY_USER_AUTHENTICATION_PASSWORD = 'Pw'
PROPERTY_USER_AUTHENTICATION_USER = 'User'
PROPERTY_USER_AUTHENTICATION_USER_ID = 'Id'
PROPERTY_USER_AUTHENTICATION_ACCESS_TOKEN = 'AccessToken'

# PLAYING_PLAY_METHOD_DIRECT_PLAY = 'DirectPlay'
PLAYING_PLAY_METHOD_DIRECT_STREAM = 'DirectStream'
# PLAYING_PLAY_METHOD_TRANSCODE = 'Transcode'

PLAYING_PROGRESS_EVENT_TIME_UPDATE = 'TimeUpdate'
PLAYING_PROGRESS_EVENT_PAUSE = 'Pause'
PLAYING_PROGRESS_EVENT_UNPAUSE = 'Unpause'
#PLAYING_PROGRESS_EVENT_VOLUME_CHANGE = 'VolumeChange'
#PLAYING_PROGRESS_EVENT_REPEAT_MODE_CHANGE = 'RepeatModeChange'
#PLAYING_PROGRESS_EVENT_AUDIO_TRACK_CHANGE = 'AudioTrackChange'
#PLAYING_PROGRESS_EVENT_SUBTITLE_TRACK_CHANGE = 'SubtitleTrackChange'
#PLAYING_PROGRESS_EVENT_PLAYLIST_ITEM_MOVE = 'PlaylistItemMove'
#PLAYING_PROGRESS_EVENT_PLAYLIST_ITEM_REMOVE = 'PlaylistItemRemove'
#PLAYING_PROGRESS_EVENT_PLAYLIST_ITEM_ADD = 'PlaylistItemAdd'
#PLAYING_PROGRESS_EVENT_QUALITY_CHANGE = 'QualityChange'
#PLAYING_PROGRESS_EVENT_STATE_CHANGE = 'StateChange'

# media provider setting identifiers and values
SETTING_PROVIDER_USER = 'emby.user'
SETTING_PROVIDER_USER_OPTION_MANUAL = 'manual'
SETTING_PROVIDER_USERNAME = 'emby.username'
SETTING_PROVIDER_PASSWORD = 'emby.password'
SETTING_PROVIDER_TEST_AUTHENTICATION = 'emby.testauthentication'
SETTING_PROVIDER_DEVICEID = 'emby.deviceid'

# media import setting identifiers and values
SETTING_IMPORT_VIEWS = 'emby.importviews'
SETTING_IMPORT_VIEWS_OPTION_ALL = 'all'
SETTING_IMPORT_VIEWS_OPTION_SPECIFIC = 'specific'
SETTING_IMPORT_VIEWS_SPECIFIC = 'emby.importspecificviews'
