# [HTTP-ENDPOINT]
from attr import fields

api_url_address = "https://www.gamedatacrunch.com"

api_steam_endpoint = "/api/steam"

api_top_performing_endpoint = "/list/all/reviews_total/"

api_top_performing_endpoint_all_fields = "/api/steam/list/all/reviews_total/?field=title,release_date,price,base_price_usd,ea_status,review,reviews_total,unfiltered_reviews_total,peak_ccu,followers,playtracker_insight_rank,current_topsellers_rank,reviews_score_fancy,metacritic_score,opencritic_score,hidden_gem_score"

# [TOP PERFORMING8

# Fields
Fields = dict(
Filtered_Reviews = "reviews_total",
All_Reviews = "unfiltered_reviews_total",
Title = "title",
Release_Date = "release_date",
Current_Price = "price",
Base_Price = "base_price_usd",
Early_Access = "ea_status",
Review_Score_Summary = "review",
Peak_CCU = "peak_ccu",
Followers = "followers",
PlayTracker_Rank = "playtracker_insight_rank",
Top_seller_rank = "current_topsellers_rank",
Adj_review = "reviews_score_fancy",
Metacritic = "metacritic_score",
Opencritic = "opencritic_score",
Hidden_score = "hidden_gem_score"
)

# [FILTERS]
api_filters_endpoint = "&filter="

# Store Categories
# Player Mode
Single_Player = dict(
Singleplayer = "sc2",
Multiplayer = "sc1",
PvP = "sc49",
Co_op = "sc9"
)

# Multiplayer
Multiplayer = dict(
Online_pvp = "sc36",
Online_co_op = "sc38",
Cross_plat_multiplayer = "sc27",
Local_pvp = "sc37",
MMO = "sc20",
Local_co_op = "sc39",
LAN_co_op = "sc48",
LAN_pvp = "sc47"
)

# Netcode
Netcode = dict(
Rollback_Netcode = "sc7700",
GGPO_Netcode = "sc7701"
)

# Controls
Controls = dict(
Full_Controller_Support = "sc28",
Partial_Controller_Support = "sc18"
)

# Steam Feature
Steam_Feature = dict(
Achievements = "sc22",
Steam_Trading_Cards = "sc29",
Cloud = "sc23",
Leaderboards = "sc25",
Steam_Workshop = "sc30"
)

# Remote Play
Remote_Play = dict(
Remote_Play_Together = "sc44",
Remote_Play_To_Tv = "sc43",
Remote_Play_To_Tablet = "sc42",
Remote_Play_To_Phone = "sc41"
)

# Released/ Unreleased
Released = dict(
Released = "re_out",
Unreleased = "re_not"
)

# Cost
Cost = dict(
Free = "pay_free",
F2P = "pay_f2p",
Paid = "pay"
)

# Early Access
EA = dict(
Early_Access_Current = "ea_cur",
Early_Access_Former = "ea_for",
Early_Access_Never = "ea_nev",
Early_Access_Unknown = "ea_unk"
)

# Platform
Platform = dict(
Windows = "win",
Macintosh = "mac",
Linux = "linux"
)

# NSFW Content
NSFW = dict(
Nudity_Sex = "mc1",
Frequent_Gore_Violence = "mc2",
Adult_Only_Sex = "mc3",
General_Mature_Content = "mc5"
)

# Price Tier
price = dict(
price_0_5 = "price_0-5",
price_5_10 = "price_5-10",
price_10_15 = "price_10-15",
price_15_30 = "price_15-30",
price_30_50 = "price_30-50",
price_50_max = "price_50-max"
)

# Release Year
Release_Year = dict(
_2000_2005 = "steam_release_year_2000-2005",
_2005_2010 = "steam_release_year_2005-2010",
_2010_2020 = "steam_release_year_2010-2020",
_2020_max = "steam_release_year_2020-max"
)

# Review Count
Review_count = dict(
_1_9 = "reviews_total_tier_1-9",
_10_49 = "reviews_total_tier_10-49",
_50_99 = "reviews_total_tier_50-99",
_100_999 = "reviews_total_tier_50-999"
)

# Top-Level Genre
top_genre = dict(
Action = "t19",
Adventure = "t21",
RPG = "t122",
Strategy = "t9",
Simulation = "t599",
Experimental = "t13782,t13782",
Racing = "t699",
Sports = "t701",
Tabletop = "t17389,t17389",
Puzzle = "t1664",
Casual = "t597"
)

# Technology
# Engine
Engine = dict(
Unity = "tk160",
XNA = "tk155",
Unknown = "tk211",
Unreal = "tk159",
GameMaker = "tk180",
RPGMaker = "tk166",
RenPy = "tk165",
Godot = "tk179",
Adobe_AIR ="tk209",
Cocos2d = "tk225",
MonoGame = "tk172",
KiriKiri = "tk175",
Construct = "tk185",
Lime_OR_OpenFL = "tk174",
AdventureGameStudio = "tk189",
FNA = "tk182",
OGRE = "tk217",
Love2D = "tk173",
CryEngine = "tk184",
Torque = "tk230",
Source = "tk162",
Solar2D = "tk223",
BlenderGameEngine = "tk232",
WolfRPGEditor = "tk156",
PlayFirstPlayground = "tk169",
Wintermute = "tk157",
idTech3 = "tk151",
Marmalade = "tk218",
TelltaleTool = "tk226",
Frostbite = "tk181",
Prism3D = "tk168",
ChromeEngine = "tk186",
Defold = "tk183",
Bitsquid = "tk220",
Kex = "tk231",
Virtools = "tk222",
Clausewitz = "tk237",
VisionaireStudio = "tk158",
GoldSource = "tk178",
idTech1 = "tk153",
Build = "tk187",
SCI = "tk164",
Pico8 = "tk170",
Heaps = "tk176",
HaemonimontSol = "tk177",
HashLink = "tk224",
Unigine = "tk202",
Source2 = "tk161",
idTech2_5 = "tk201",
idTech6 = "tk148",
idTech0 = "tk154",
Aurora = "tk188",
AGI = "tk192",
RAGE = "tk216",
idTech5 = "tk149",
idTech4 = "tk150",
Infinity = "tk203",
Snowdrop = "tk163",
Danmakufu = "tk240",
Flexi = "tk219",
idTech2 = "tk152",
Phyre = "tk171",
idTech7 = "tk207"
)

# SDK 
SDK = dict(
Unknown = "tk210",
NodeJS = "tk139",
CEF = "tk200",
SDL = "tk137" ,
OpenVR = "tk215",
OpenAL = "tk229",
FMOD = "tk144",
Photon = "tk238",
NVIDIA_Physx = "tk140",
Adobe_Flash = "tk206",
NVIDIA_Nsight_Aftermath = "tk141",
Discord = "tk146",
CRIWARE = "tk204",
Bink_Video = "tk221",
Wwise = "tk227",
UnityURP = "tk233",
JVM = "tk236",
Qt = "tk138",
EpicOnlineServices = "tk145",
SteamworksNET = "tk239"
)

# EMULATOR
Emulator = dict(
Unknown = "tk212",
DOSBOX = "tk194",
SCUMMVM = "tk193"
)

# CONTAINER
Container = dict(
Unknown = "tk213",
Electron = "tk195"
)

# ANTI-CHEAT
Anti_Cheat = dict(
Unknown = "tk214",
EasyAntiCheat = "tk198",
XIGNCODE3 = "tk234",
BattlEye = "tk199",
nProtectGameGuard = "tk196",
PunkBuster = "tk197",
EQU8 = "tk235"
)


sorted_values = sorted(top_genre.values())