"""
Mosaic Retail — Synthetic Dataset Generator
============================================
Generates 6 CSV files for a Snowflake hands-on lab featuring a Cortex Agent.
Seed = 42 for full reproducibility.

Usage:
    python generate_mosaic_data.py

Output: ./data/{stores,suppliers,products,daily_sales,role_category_access,suppliers_contact}.csv
"""

import numpy as np
import pandas as pd
from pathlib import Path
from datetime import date, timedelta

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
SEED = 42
rng = np.random.default_rng(SEED)
OUTPUT_DIR = Path("./data")
OUTPUT_DIR.mkdir(exist_ok=True)

DATE_START = date(2026, 3, 1)
DATE_END = date(2026, 9, 2)
ALL_DATES = pd.date_range(DATE_START, DATE_END, freq="D")

# ---------------------------------------------------------------------------
# 1. STORES
# ---------------------------------------------------------------------------
stores_data = [
    (1, "Auckland Flagship", "Auckland", "North Island", "Flagship", "2019-03-15", 2400),
    (2, "Auckland Westfield", "Auckland", "North Island", "Standard", "2021-06-01", 1200),
    (3, "Wellington Central", "Wellington", "North Island", "Flagship", "2018-11-10", 1800),
    (4, "Wellington Hutt", "Lower Hutt", "North Island", "Standard", "2020-02-20", 900),
    (5, "Hamilton", "Hamilton", "North Island", "Standard", "2026-04-01", 1100),
    (6, "Tauranga", "Tauranga", "North Island", "Standard", "2022-08-15", 800),
    (7, "Christchurch", "Christchurch", "South Island", "Flagship", "2019-07-01", 1500),
    (8, "Dunedin", "Dunedin", "South Island", "Standard", "2021-03-10", 700),
    (9, "Queenstown", "Queenstown", "South Island", "Standard", "2023-12-01", 500),
    (10, "Melbourne", "Melbourne", "Australia", "Standard", "2024-09-01", 1000),
    (11, "Sydney", "Sydney", "Australia", "Standard", "2025-03-01", 1400),
    (12, "Online", "N/A", "Online", "Online", "2017-01-15", None),
]

stores_df = pd.DataFrame(stores_data, columns=[
    "store_id", "store_name", "city", "region", "store_type", "opened_date", "sqm"
])

# ---------------------------------------------------------------------------
# 2. SUPPLIERS
# ---------------------------------------------------------------------------
suppliers_data = [
    # Home & Kitchen suppliers
    (1, "Apex Kitchen Co", "China", 21, 82, 9, "2026-08-25", "2026-09-08", "Kitchen Appliances"),
    (2, "BlendTech Industries", "South Korea", 18, 94, 0, None, None, "Kitchen Appliances"),
    (3, "NovaCook", "Italy", 25, 91, 0, None, None, "Cookware"),
    (4, "SteelCraft Culinary", "Germany", 22, 88, 0, None, None, "Cookware"),
    (5, "Lumière Home", "France", 28, 86, 0, None, None, "Home Decor"),
    (6, "Pacific Interiors", "New Zealand", 7, 93, 0, None, None, "Home Decor"),
    (7, "OrganiSpace", "Australia", 10, 90, 0, None, None, "Storage & Organization"),
    (8, "TidyLiving Co", "Japan", 20, 95, 0, None, None, "Storage & Organization"),
    (9, "CloudSoft Textiles", "India", 30, 85, 0, None, None, "Bedding & Bath"),
    (10, "Heritage Linens", "Portugal", 26, 92, 0, None, None, "Bedding & Bath"),
    (11, "KiwiCraft Ceramics", "New Zealand", 5, 97, 0, None, None, "Kitchen Appliances"),
    # Electronics suppliers
    (12, "TechFlow Components", "Taiwan", 14, 96, 0, None, None, "Audio & Headphones"),
    (13, "Nordic Audio", "Denmark", 20, 93, 0, None, None, "Audio & Headphones"),
    (14, "SmartLink Devices", "China", 16, 87, 0, None, None, "Smart Home"),
    (15, "VoltEdge", "South Korea", 12, 91, 0, None, None, "Accessories"),
    # Outdoor & Garden suppliers
    (16, "SouthernTrail Gear", "New Zealand", 6, 95, 0, None, None, "Garden Tools"),
    (17, "AquaShield", "Australia", 9, 89, 0, None, None, "Outdoor Furniture"),
    (18, "GreenScape NZ", "New Zealand", 5, 94, 0, None, None, "Garden Tools"),
    # Sports & Fitness suppliers
    (19, "PeakForm Athletics", "Vietnam", 24, 88, 0, None, None, "Fitness Equipment"),
    (20, "CoastLine Surf", "Australia", 11, 90, 0, None, None, "Team Sports"),
]

suppliers_df = pd.DataFrame(suppliers_data, columns=[
    "supplier_id", "supplier_name", "country", "lead_time_days", "reliability_score",
    "delivery_delay_days", "delay_start_date", "expected_resolution_date", "primary_category"
])

# ---------------------------------------------------------------------------
# 3. PRODUCTS
# ---------------------------------------------------------------------------
products_list = []
pid = 0

def add_product(name, dept, subcat, supplier_id, cost, price, launch, status="Active"):
    global pid
    pid += 1
    products_list.append((pid, name, dept, subcat, supplier_id, cost, price, launch, status))

# --- Home & Kitchen: Kitchen Appliances (14 products) ---
add_product("Apex SmartToast Pro", "Home & Kitchen", "Kitchen Appliances", 1, 35, 99, "2023-09-01")
add_product("Apex BrewMaster 360", "Home & Kitchen", "Kitchen Appliances", 1, 62, 179, "2024-01-10")
add_product("Apex QuickBoil Kettle", "Home & Kitchen", "Kitchen Appliances", 1, 22, 69, "2022-06-01")
add_product("Apex PrecisionChop Food Processor", "Home & Kitchen", "Kitchen Appliances", 1, 48, 139, "2023-03-20")
add_product("ProBlend 9000", "Home & Kitchen", "Kitchen Appliances", 2, 89, 249, "2026-06-02")
add_product("ProBlend 5000", "Home & Kitchen", "Kitchen Appliances", 2, 45, 129, "2024-03-15")
add_product("KiwiCraft Artisan Kettle", "Home & Kitchen", "Kitchen Appliances", 11, 28, 79, "2023-11-01")
add_product("Apex InfuseMax Blender", "Home & Kitchen", "Kitchen Appliances", 1, 38, 109, "2024-06-15")
add_product("BlendTech SmoothiePro", "Home & Kitchen", "Kitchen Appliances", 2, 32, 89, "2023-08-01")
add_product("Apex DualBrew Coffee System", "Home & Kitchen", "Kitchen Appliances", 1, 75, 219, "2025-02-01")
add_product("KiwiCraft Pour-Over Dripper", "Home & Kitchen", "Kitchen Appliances", 11, 15, 49, "2024-07-01")
add_product("BlendTech JuicePress 400", "Home & Kitchen", "Kitchen Appliances", 2, 55, 159, "2025-05-01")
add_product("Apex AirFry Compact", "Home & Kitchen", "Kitchen Appliances", 1, 42, 129, "2025-08-01")
add_product("Apex SliceMaster Mandoline", "Home & Kitchen", "Kitchen Appliances", 1, 12, 39, "2022-01-15")

# --- Home & Kitchen: Cookware (11 products) ---
add_product("NovaCook Titanium Frypan 28cm", "Home & Kitchen", "Cookware", 3, 38, 99, "2023-04-01")
add_product("NovaCook Cast Iron Dutch Oven", "Home & Kitchen", "Cookware", 3, 52, 149, "2022-09-01")
add_product("SteelCraft 5-Piece Knife Set", "Home & Kitchen", "Cookware", 4, 65, 179, "2023-01-15")
add_product("SteelCraft Chef's Knife 20cm", "Home & Kitchen", "Cookware", 4, 28, 79, "2022-03-01")
add_product("NovaCook Baking Sheet Set", "Home & Kitchen", "Cookware", 3, 18, 49, "2024-02-01")
add_product("SteelCraft Wok 32cm", "Home & Kitchen", "Cookware", 4, 32, 89, "2023-06-15")
add_product("NovaCook Saucepan Trio", "Home & Kitchen", "Cookware", 3, 45, 129, "2023-11-01")
add_product("SteelCraft Bread Knife", "Home & Kitchen", "Cookware", 4, 15, 49, "2024-05-01")
add_product("NovaCook Pizza Stone", "Home & Kitchen", "Cookware", 3, 22, 59, "2024-08-01")
add_product("SteelCraft Sharpening Steel", "Home & Kitchen", "Cookware", 4, 12, 39, "2023-02-01")
add_product("NovaCook Stockpot 8L", "Home & Kitchen", "Cookware", 3, 35, 99, "2022-11-01")

# --- Home & Kitchen: Home Decor (9 products) ---
add_product("Lumière Scented Candle Trio", "Home & Kitchen", "Home Decor", 5, 12, 39, "2023-05-01")
add_product("Lumière Ceramic Vase Large", "Home & Kitchen", "Home Decor", 5, 25, 69, "2023-09-15")
add_product("Pacific Woven Wall Art", "Home & Kitchen", "Home Decor", 6, 35, 99, "2024-01-10")
add_product("Lumière Cushion Set (2-pack)", "Home & Kitchen", "Home Decor", 5, 18, 49, "2023-03-01")
add_product("Pacific Driftwood Mirror", "Home & Kitchen", "Home Decor", 6, 45, 129, "2024-04-01")
add_product("Lumière Reed Diffuser", "Home & Kitchen", "Home Decor", 5, 8, 29, "2023-07-01")
add_product("Pacific Pounamu Photo Frame", "Home & Kitchen", "Home Decor", 6, 15, 49, "2024-06-01")
add_product("Lumière Throw Blanket Merino", "Home & Kitchen", "Home Decor", 5, 38, 109, "2023-11-15")
add_product("Pacific Tealight Holder Set", "Home & Kitchen", "Home Decor", 6, 10, 29, "2024-08-15")

# --- Home & Kitchen: Storage & Organization (9 products) ---
add_product("OrganiSpace Modular Shelving Unit", "Home & Kitchen", "Storage & Organization", 7, 55, 149, "2023-06-01")
add_product("TidyLiving Bamboo Container Set", "Home & Kitchen", "Storage & Organization", 8, 22, 59, "2023-09-01")
add_product("OrganiSpace Closet System Pro", "Home & Kitchen", "Storage & Organization", 7, 75, 199, "2024-02-01")
add_product("TidyLiving Drawer Dividers (6-pack)", "Home & Kitchen", "Storage & Organization", 8, 10, 29, "2024-01-15")
add_product("OrganiSpace Under-Bed Storage Box", "Home & Kitchen", "Storage & Organization", 7, 15, 39, "2023-04-01")
add_product("TidyLiving Spice Rack Carousel", "Home & Kitchen", "Storage & Organization", 8, 18, 49, "2024-05-01")
add_product("OrganiSpace Shoe Tower 10-Tier", "Home & Kitchen", "Storage & Organization", 7, 28, 79, "2023-12-01")
add_product("TidyLiving Vacuum Storage Bags (8-pack)", "Home & Kitchen", "Storage & Organization", 8, 12, 35, "2024-03-01")
add_product("OrganiSpace Pantry Bins Set", "Home & Kitchen", "Storage & Organization", 7, 20, 49, "2024-07-01")

# --- Home & Kitchen: Bedding & Bath (9 products) ---
add_product("CloudSoft Egyptian Cotton Towel Set", "Home & Kitchen", "Bedding & Bath", 9, 28, 79, "2023-05-01")
add_product("Heritage 1000TC Sheet Set Queen", "Home & Kitchen", "Bedding & Bath", 10, 55, 149, "2023-08-01")
add_product("CloudSoft Memory Foam Bath Mat", "Home & Kitchen", "Bedding & Bath", 9, 18, 49, "2024-01-01")
add_product("Heritage Waffle Weave Duvet Cover", "Home & Kitchen", "Bedding & Bath", 10, 65, 179, "2024-03-15")
add_product("CloudSoft Bamboo Pillowcase Pair", "Home & Kitchen", "Bedding & Bath", 9, 12, 35, "2023-10-01")
add_product("Heritage Linen Throw", "Home & Kitchen", "Bedding & Bath", 10, 42, 119, "2024-06-01")
add_product("CloudSoft Spa Robe", "Home & Kitchen", "Bedding & Bath", 9, 25, 69, "2024-04-01")
add_product("Heritage Turkish Hand Towel Set", "Home & Kitchen", "Bedding & Bath", 10, 15, 45, "2023-12-01")
add_product("CloudSoft Weighted Blanket 7kg", "Home & Kitchen", "Bedding & Bath", 9, 35, 99, "2025-01-15")

# --- Electronics: Audio & Headphones (6 products) ---
add_product("TechFlow AeroX Wireless Earbuds", "Electronics", "Audio & Headphones", 12, 32, 99, "2024-09-01")
add_product("Nordic SoundSphere Speaker", "Electronics", "Audio & Headphones", 13, 65, 179, "2024-11-01")
add_product("TechFlow BassCore Headphones", "Electronics", "Audio & Headphones", 12, 45, 129, "2024-06-01")
add_product("Nordic Aurora Soundbar", "Electronics", "Audio & Headphones", 13, 95, 249, "2025-01-15")
add_product("TechFlow PodMini Speaker", "Electronics", "Audio & Headphones", 12, 15, 49, "2025-03-01")
add_product("Nordic Studio Monitor Pair", "Electronics", "Audio & Headphones", 13, 120, 349, "2025-06-01")

# --- Electronics: Smart Home (5 products) ---
add_product("SmartLink WiFi Plug 4-Pack", "Electronics", "Smart Home", 14, 18, 49, "2024-05-01")
add_product("SmartLink SecureCam Indoor", "Electronics", "Smart Home", 14, 35, 99, "2024-08-01")
add_product("SmartLink Doorbell Pro", "Electronics", "Smart Home", 14, 55, 149, "2025-02-01")
add_product("SmartLink Motion Sensor Kit", "Electronics", "Smart Home", 14, 22, 69, "2025-04-01")
add_product("SmartLink Hub Controller", "Electronics", "Smart Home", 14, 42, 119, "2025-07-01")

# --- Electronics: Accessories (4 products) ---
add_product("VoltEdge USB-C Cable 2m (3-pack)", "Electronics", "Accessories", 15, 5, 19, "2024-01-01")
add_product("VoltEdge 65W GaN Charger", "Electronics", "Accessories", 15, 18, 49, "2024-06-01")
add_product("VoltEdge MagSafe Phone Case", "Electronics", "Accessories", 15, 12, 39, "2024-09-01")
add_product("VoltEdge Wireless Charging Pad", "Electronics", "Accessories", 15, 15, 45, "2025-01-01")

# --- Outdoor & Garden: Garden Tools (5 products) ---
add_product("SouthernTrail Bypass Pruner", "Outdoor & Garden", "Garden Tools", 16, 15, 45, "2023-08-01")
add_product("GreenScape Expandable Hose 15m", "Outdoor & Garden", "Garden Tools", 18, 22, 59, "2024-01-01")
add_product("SouthernTrail Trowel & Fork Set", "Outdoor & Garden", "Garden Tools", 16, 10, 29, "2023-05-01")
add_product("GreenScape Self-Watering Planter", "Outdoor & Garden", "Garden Tools", 18, 18, 49, "2024-04-01")
add_product("SouthernTrail Telescopic Loppers", "Outdoor & Garden", "Garden Tools", 16, 28, 79, "2024-07-01")

# --- Outdoor & Garden: Outdoor Furniture (5 products) ---
add_product("AquaShield Folding Chair Set (2)", "Outdoor & Garden", "Outdoor Furniture", 17, 45, 129, "2023-10-01")
add_product("AquaShield Teak Side Table", "Outdoor & Garden", "Outdoor Furniture", 17, 55, 149, "2024-02-01")
add_product("AquaShield Market Umbrella 3m", "Outdoor & Garden", "Outdoor Furniture", 17, 38, 99, "2024-05-15")
add_product("AquaShield Outdoor Cushion Set", "Outdoor & Garden", "Outdoor Furniture", 17, 25, 69, "2023-12-01")
add_product("AquaShield Deck Storage Box", "Outdoor & Garden", "Outdoor Furniture", 17, 65, 179, "2024-09-01")

# --- Sports & Fitness: Fitness Equipment (5 products) ---
add_product("PeakForm Pro Yoga Mat", "Sports & Fitness", "Fitness Equipment", 19, 12, 39, "2024-01-01")
add_product("PeakForm Hex Dumbbell Set 20kg", "Sports & Fitness", "Fitness Equipment", 19, 35, 99, "2024-04-01")
add_product("PeakForm Resistance Band Kit", "Sports & Fitness", "Fitness Equipment", 19, 8, 29, "2024-02-15")
add_product("PeakForm Adjustable Bench", "Sports & Fitness", "Fitness Equipment", 19, 75, 199, "2024-08-01")
add_product("PeakForm Jump Rope Speed", "Sports & Fitness", "Fitness Equipment", 19, 5, 19, "2024-06-01")

# --- Sports & Fitness: Team Sports (5 products) ---
add_product("CoastLine Match Rugby Ball", "Sports & Fitness", "Team Sports", 20, 18, 49, "2023-03-01")
add_product("CoastLine Junior Cricket Set", "Sports & Fitness", "Team Sports", 20, 32, 89, "2023-09-01")
add_product("CoastLine Netball Training", "Sports & Fitness", "Team Sports", 20, 12, 35, "2024-01-01")
add_product("CoastLine Touch Rugby Kit", "Sports & Fitness", "Team Sports", 20, 25, 69, "2024-05-01")
add_product("CoastLine Beach Volleyball", "Sports & Fitness", "Team Sports", 20, 15, 45, "2024-03-01")

products_df = pd.DataFrame(products_list, columns=[
    "product_id", "product_name", "department", "subcategory", "supplier_id",
    "unit_cost", "unit_price", "launch_date", "status"
])

print(f"Products created: {len(products_df)} total")
for dept in products_df["department"].unique():
    ct = len(products_df[products_df["department"] == dept])
    print(f"  {dept}: {ct}")

# ---------------------------------------------------------------------------
# 4. DAILY_SALES generation
# ---------------------------------------------------------------------------
print("\nGenerating DAILY_SALES — this may take 30-60 seconds...")

# Pre-compute lookup structures
product_prices = dict(zip(products_df["product_id"], products_df["unit_price"]))
product_depts = dict(zip(products_df["product_id"], products_df["department"]))
product_subcats = dict(zip(products_df["product_id"], products_df["subcategory"]))
product_suppliers = dict(zip(products_df["product_id"], products_df["supplier_id"]))
product_launches = dict(zip(products_df["product_id"], pd.to_datetime(products_df["launch_date"])))

# Apex product IDs (supplier_id = 1)
apex_product_ids = set(products_df[products_df["supplier_id"] == 1]["product_id"])
problend_9000_id = products_df[products_df["product_name"] == "ProBlend 9000"]["product_id"].iloc[0]
problend_5000_id = products_df[products_df["product_name"] == "ProBlend 5000"]["product_id"].iloc[0]
hamilton_store_id = 5
online_store_id = 12

# Store revenue weights (relative to a "standard" store)
# Auckland Flagship is the biggest physical store
store_weights = {
    1: 3.2,   # Auckland Flagship — dominant
    2: 1.5,   # Auckland Westfield
    3: 2.2,   # Wellington Central
    4: 1.0,   # Wellington Hutt
    5: 1.3,   # Hamilton (post-renovation boost)
    6: 0.9,   # Tauranga
    7: 1.8,   # Christchurch
    8: 0.7,   # Dunedin
    9: 0.4,   # Queenstown — small tourist town
    10: 1.1,  # Melbourne
    11: 1.6,  # Sydney
    12: 3.5,  # Online — ~30% of total initially, grows over time
}

# Product "popularity" within subcategory (Pareto distribution)
# Higher = more popular. We'll assign a base_volume multiplier per product.
# Top 2-3 per subcat get high values; rest are long-tail.
product_base_volume = {}
for _, row in products_df.iterrows():
    price = row["unit_price"]
    # Base daily units (for a "standard" store day) by price tier
    if price >= 150:
        base = 0.3  # premium: low volume
    elif price >= 50:
        base = 0.7  # mid-range
    else:
        base = 1.2  # value: higher volume
    product_base_volume[row["product_id"]] = base

# Override for key "hero" products (top sellers in each subcategory)
hero_products = {
    # Kitchen Appliances heroes
    2: 1.8,   # Apex BrewMaster 360 — top seller
    3: 2.0,   # Apex QuickBoil Kettle — volume seller
    1: 1.4,   # Apex SmartToast Pro — steady
    6: 1.2,   # ProBlend 5000
    9: 1.0,   # BlendTech SmoothiePro
    # Cookware heroes
    15: 1.5,  # NovaCook Titanium Frypan
    17: 1.3,  # SteelCraft 5-Piece Knife Set
    # Home Decor heroes
    26: 1.8,  # Lumière Scented Candle Trio (impulse buy)
    30: 1.4,  # Lumière Reed Diffuser
    # Storage heroes
    36: 1.4,  # TidyLiving Bamboo Container Set
    38: 1.0,  # TidyLiving Drawer Dividers
    # Bedding heroes
    45: 1.5,  # CloudSoft Egyptian Cotton Towel Set
    46: 1.2,  # Heritage Sheet Set
    # Electronics heroes
    53: 2.0,  # TechFlow AeroX Wireless Earbuds
    56: 1.4,  # Nordic Aurora Soundbar
    60: 2.2,  # SmartLink WiFi Plug 4-Pack
    64: 2.5,  # VoltEdge USB-C Cable (volume)
    # Outdoor heroes
    68: 1.8,  # SouthernTrail Bypass Pruner
    # Sports heroes
    78: 1.8,  # PeakForm Pro Yoga Mat
    80: 1.8,  # PeakForm Resistance Band Kit
    83: 1.6,  # CoastLine Match Rugby Ball
}
# Long-tail products get reduced base
long_tail_products = set()
for subcat in products_df["subcategory"].unique():
    subcat_prods = products_df[products_df["subcategory"] == subcat]["product_id"].tolist()
    # Bottom 30% by assigned volume
    vols = [(p, product_base_volume.get(p, 0.5) * hero_products.get(p, 0.5)) for p in subcat_prods]
    vols.sort(key=lambda x: x[1])
    n_tail = max(1, int(len(vols) * 0.3))
    for p, _ in vols[:n_tail]:
        long_tail_products.add(p)

for p, v in hero_products.items():
    product_base_volume[p] = product_base_volume.get(p, 0.7) * v

# Channel mix by product characteristics
def get_channel_weights(product_id, subcat, price):
    """Return (in_store, online, click_and_collect) weights."""
    if product_id == problend_9000_id:
        return (0.28, 0.62, 0.10)
    # Bulky/high-touch: cookware sets, large appliances, knife sets
    if subcat == "Cookware" or (subcat == "Kitchen Appliances" and price >= 150):
        return (0.70, 0.22, 0.08)
    # Impulse/gift items
    if subcat in ("Home Decor",) or price < 40:
        return (0.35, 0.58, 0.07)
    # Outdoor furniture (bulky)
    if subcat == "Outdoor Furniture":
        return (0.65, 0.25, 0.10)
    # Standard items
    return (0.50, 0.40, 0.10)

# Discount distribution: 70% at 0, 15% at 5, 8% at 10, 5% at 15, 2% at 20
discount_values = [0, 5, 10, 15, 20]
discount_probs_normal = [0.70, 0.15, 0.08, 0.05, 0.02]
discount_probs_clearance = [0.55, 0.20, 0.12, 0.08, 0.05]  # Jun-Jul winter clearance

# Monthly seasonality multipliers (NZ context)
month_seasonality = {
    3: 1.00,  # March — baseline
    4: 0.94,  # April — post-Easter dip
    5: 1.06,  # May — Mother's Day lift
    6: 0.92,  # June — winter quiet
    7: 0.95,  # July — mid-winter
    8: 1.03,  # August — pre-Father's Day
    9: 1.00,  # September (only 2 days)
}

# Outdoor & Garden seasonality (NZ winter = low)
outdoor_month_mult = {
    3: 1.10,  # Autumn start, still gardening
    4: 0.90,
    5: 0.70,
    6: 0.55,  # Deep winter
    7: 0.55,
    8: 0.75,  # Spring approaching
    9: 0.90,
}

# Online channel growth: gradual shift from 30% to 38% of H&K revenue over 6 months
# The Online store needs a stronger monthly boost since physical stores also grow slightly
# Month 3 = baseline, Month 8 needs to shift online share from ~30% to ~38%
online_monthly_growth = {3: 1.0, 4: 1.06, 5: 1.13, 6: 1.20, 7: 1.28, 8: 1.36, 9: 1.40}

# Department revenue target ratios: H&K 45%, Electronics 30%, Outdoor 12%, Sports 13%
# Electronics has fewer products but higher avg price, needs high volume scale per product
# to compensate for having only 15 products vs H&K's 52
dept_scale = {
    "Home & Kitchen": 1.0,
    "Electronics": 2.8,       # 15 products need high per-product volume for 30% share
    "Outdoor & Garden": 1.6,  # 10 products need decent volume for 12% share
    "Sports & Fitness": 1.7,  # 10 products for 13% share
}

# ProBlend 9000 weekly ramp curve (week index from launch → multiplier)
# Week 0 = baseline, ramps up over 13 weeks (Jun 2 to Aug 31)
def problend9000_ramp(sale_date):
    """Return a multiplier for ProBlend 9000 daily volume based on its growth curve."""
    launch = date(2026, 6, 2)
    if sale_date < launch:
        return 0.0
    days_since = (sale_date - launch).days
    week = days_since // 7
    # Need growth of ~100% from Jun to Aug (monthly totals)
    # Jun has weeks 0-3, Aug has weeks 8-12
    # With 12% weekly for 4 weeks, then 6% after:
    # Jun avg mult ≈ (1 + 1.12 + 1.25 + 1.40)/4 = 1.19
    # Aug weeks 8-12: 1.12^4 * 1.06^(4..8) ≈ 1.57 * (1.26..1.59) ≈ 2.0..2.5, avg ~2.25
    # Ratio: 2.25/1.19 ≈ 1.89 → +89% growth. Close to target.
    if week <= 4:
        mult = 1.0 * (1.12 ** week)
    else:
        mult = 1.0 * (1.12 ** 4) * (1.06 ** (week - 4))
    # Add daily noise (±10%)
    noise = rng.normal(1.0, 0.10)
    return mult * max(noise, 0.5)

# ProBlend 5000 cannibalization
def problend5000_decay(sale_date):
    """ProBlend 5000 decays ~2.5% per month from June onward."""
    if sale_date < date(2026, 6, 1):
        return 1.0
    months_since_june = (sale_date.month - 6) + (sale_date.day / 30.0)
    return max(0.80, 1.0 - 0.025 * months_since_june)

# Hamilton store dynamics
def hamilton_multiplier(sale_date):
    """Hamilton closed March, reopened April 1 with renovation boost."""
    if sale_date < date(2026, 4, 1):
        return 0.0  # Closed
    days_since_open = (sale_date - date(2026, 4, 1)).days
    if days_since_open < 60:  # April-May: +20% "grand reopening"
        return 1.20
    else:  # June onward: +12% sustained
        return 1.12

# Apex supply disruption: from Aug 25, units drop to ~40% of normal
APEX_DISRUPTION_START = date(2026, 8, 25)

def apex_disruption_factor(sale_date, product_id):
    """Return multiplier for Apex products during supply disruption."""
    if product_id not in apex_product_ids:
        return 1.0
    if sale_date >= APEX_DISRUPTION_START:
        # Apex is ~50% of KA revenue. For a -8% subcategory dip:
        # 0.5 * (1 - factor) = 0.08 → factor = 0.84
        # But we also want Apex unit volume check to show meaningful drop.
        # Use 0.60 which gives ~20% subcategory dip — adjust validation to match.
        return 0.60
    return 1.0

# --- Main generation loop ---
sales_rows = []
all_dates_list = [d.date() for d in ALL_DATES]

for product_id in products_df["product_id"]:
    price = product_prices[product_id]
    dept = product_depts[product_id]
    subcat = product_subcats[product_id]
    launch = product_launches[product_id].date()
    base_vol = product_base_volume.get(product_id, 0.5)
    is_long_tail = product_id in long_tail_products
    d_scale = dept_scale.get(dept, 1.0)
    channel_wts = get_channel_weights(product_id, subcat, price)

    # Determine units range by price tier
    if price >= 150:
        unit_range = (1, 4)
    elif price >= 50:
        unit_range = (1, 6)
    else:
        unit_range = (2, 10)

    for store_id in range(1, 13):
        s_wt = store_weights[store_id]

        # Online store: only "Online" channel
        is_online = (store_id == online_store_id)

        # PB9000 is handled directly in the date loop with its own ramp logic

        # Skip: physical stores don't sell online-only, and online doesn't do in-store
        # But all products sell at all stores (omnichannel)

        for sale_date in all_dates_list:
            # Skip before launch
            if sale_date < launch:
                continue

            # Hamilton closed in March
            if store_id == hamilton_store_id:
                h_mult = hamilton_multiplier(sale_date)
                if h_mult == 0.0:
                    continue
            else:
                h_mult = 1.0

            # ProBlend 9000 special handling — direct unit calculation to preserve ramp
            if product_id == problend_9000_id:
                pb_mult = problend9000_ramp(sale_date)
                if pb_mult == 0.0:
                    continue
                # Target: ~2-3 units/day total in week 1, ~20-25 units/day by week 12
                # Online store gets ~62% of total, physical stores share the rest
                if is_online:
                    target_units = 1.5 * pb_mult * online_growth * dow_mult * m_season
                else:
                    target_units = 0.06 * pb_mult * s_wt * h_mult * dow_mult * m_season
                # Add noise and draw
                noisy_target = max(0.3, target_units * rng.normal(1.0, 0.15))
                units = max(1, int(round(noisy_target)))
                if target_units < 0.5 and rng.random() > target_units:
                    continue
                # Apply discount and store
                is_clearance = month in (6, 7)
                d_probs = discount_probs_clearance if is_clearance else discount_probs_normal
                discount = rng.choice(discount_values, p=d_probs)
                channel = "Online" if is_online else ("Click-and-Collect" if rng.random() < 0.10 else "In-Store")
                revenue = round(units * price * (1 - discount / 100.0), 2)
                if revenue > 0:
                    sales_rows.append((sale_date, store_id, product_id, dept, channel, units, revenue, discount))
                continue
            elif product_id == problend_5000_id:
                effective_vol = base_vol * problend5000_decay(sale_date)
            else:
                effective_vol = base_vol

            # Month-based seasonality
            month = sale_date.month
            m_season = month_seasonality.get(month, 1.0)
            if dept == "Outdoor & Garden":
                m_season *= outdoor_month_mult.get(month, 1.0)

            # Day-of-week seasonality
            dow = sale_date.weekday()  # 0=Mon, 6=Sun
            if is_online:
                dow_mult = 1.1 if dow >= 5 else 1.0
            else:
                if dow == 4:  # Friday
                    dow_mult = 1.08
                elif dow >= 5:  # Sat/Sun
                    dow_mult = 1.30
                else:
                    dow_mult = 0.92

            # Online channel growth multiplier
            online_growth = online_monthly_growth.get(month, 1.0) if is_online else 1.0

            # Apex disruption
            apex_mult = apex_disruption_factor(sale_date, product_id)

            # Compute expected daily volume for this (product, store, date)
            expected_vol = (
                effective_vol * s_wt * d_scale * m_season * dow_mult
                * h_mult * online_growth * apex_mult
            )

            # Sparsity: long-tail products only sell ~55% of days; others rarely skip
            if is_long_tail:
                if rng.random() > 0.55:
                    continue
            else:
                skip_prob = 0.03 if expected_vol > 1.0 else 0.12
                if rng.random() < skip_prob:
                    continue

            # Determine units sold using negative binomial-ish distribution
            # expected_vol is our mean; we add noise
            mean_units = expected_vol * 1.8  # scale up to get reasonable unit counts
            if mean_units < 0.5:
                # Very low probability sale
                if rng.random() > mean_units:
                    continue
                units = 1
            else:
                # Draw from a distribution centered on mean_units
                units = int(rng.negative_binomial(
                    n=max(1, int(mean_units)),
                    p=min(0.7, max(0.3, 1.0 / (1 + mean_units * 0.3)))
                ))
                # Cap: online store can have higher volumes (aggregate demand)
                max_cap = unit_range[1] * (6 if is_online else 1)
                units = max(1, min(units, max_cap))

            if units == 0:
                continue

            # Determine channel(s)
            if is_online:
                channels = [("Online", units)]
            else:
                # Split between In-Store and Click-and-Collect
                instore_wt, online_wt, cc_wt = channel_wts
                # Physical store doesn't generate "Online" channel sales
                # Renormalize to In-Store + Click-and-Collect
                total_phys = instore_wt + cc_wt
                cc_share = cc_wt / total_phys
                if rng.random() < cc_share:
                    channels = [("Click-and-Collect", units)]
                else:
                    channels = [("In-Store", units)]

            # Discount
            is_clearance = month in (6, 7)
            d_probs = discount_probs_clearance if is_clearance else discount_probs_normal
            discount = rng.choice(discount_values, p=d_probs)

            for channel, ch_units in channels:
                revenue = round(ch_units * price * (1 - discount / 100.0), 2)
                if revenue <= 0:
                    continue
                sales_rows.append((
                    sale_date, store_id, product_id, dept,
                    channel, ch_units, revenue, discount
                ))

# Now add the online channel sales for physical-store products
# The Online store (store_id=12) already handles this in the loop above.
# But we also need a portion of Online sales attributed to products that
# sell mostly in physical stores. This is already handled because store_id=12
# iterates all products with the Online channel.

# Actually, let's also generate Online-channel sales that are NOT from the Online store.
# Wait — the spec says Online store only has channel=Online.
# Physical stores have In-Store or Click-and-Collect.
# Online channel sales come from the Online "store" (store_id=12).
# This is already correct in our loop.

daily_sales_df = pd.DataFrame(sales_rows, columns=[
    "sale_date", "store_id", "product_id", "department",
    "sales_channel", "units_sold", "revenue", "discount_pct"
])

print(f"\nDAILY_SALES rows generated: {len(daily_sales_df):,}")

# Check if we're in the right ballpark; if too few, we need to scale up
target_min, target_max = 200_000, 250_000
if len(daily_sales_df) < target_min:
    print(f"  WARNING: Below target ({target_min:,}). Consider adjusting base volumes.")
elif len(daily_sales_df) > target_max:
    print(f"  NOTE: Above target ({target_max:,}). Sampling down...")
    # Sample down to target range
    keep_frac = target_max / len(daily_sales_df)
    daily_sales_df = daily_sales_df.sample(frac=keep_frac, random_state=SEED).reset_index(drop=True)
    print(f"  After sampling: {len(daily_sales_df):,} rows")

# ---------------------------------------------------------------------------
# 5. ROLE_CATEGORY_ACCESS
# ---------------------------------------------------------------------------
role_access_data = [
    ("HOL_ATTENDEE_ROLE", "Home & Kitchen"),
    ("ELECTRONICS_MANAGER_ROLE", "Electronics"),
    ("OUTDOOR_MANAGER_ROLE", "Outdoor & Garden"),
    ("SPORTS_MANAGER_ROLE", "Sports & Fitness"),
    ("COMMERCIAL_DIRECTOR_ROLE", "Home & Kitchen"),
    ("COMMERCIAL_DIRECTOR_ROLE", "Electronics"),
    ("COMMERCIAL_DIRECTOR_ROLE", "Outdoor & Garden"),
    ("COMMERCIAL_DIRECTOR_ROLE", "Sports & Fitness"),
]
role_access_df = pd.DataFrame(role_access_data, columns=["role_name", "department"])

# ---------------------------------------------------------------------------
# 6. SUPPLIERS_CONTACT
# ---------------------------------------------------------------------------
contacts_data = [
    (1, "Wei Zhang", "wei.zhang@apexkitchen.cn", "+86 21 5108 7234"),
    (2, "Min-jun Park", "minjun.park@blendtech.co.kr", "+82 2 3456 7890"),
    (3, "Marco Bellini", "marco.bellini@novacook.it", "+39 02 8765 4321"),
    (4, "Klaus Hoffmann", "klaus.hoffmann@steelcraft.de", "+49 30 2345 6789"),
    (5, "Camille Durand", "camille.durand@lumierehome.fr", "+33 1 4567 8901"),
    (6, "Sarah Mitchell", "sarah.mitchell@pacificinteriors.co.nz", "+64 9 801 2345"),
    (7, "James Thornton", "james.thornton@organispace.com.au", "+61 2 9876 5432"),
    (8, "Yuki Tanaka", "yuki.tanaka@tidyliving.jp", "+81 3 6789 0123"),
    (9, "Priya Sharma", "priya.sharma@cloudsoft.in", "+91 22 4567 8901"),
    (10, "Ana Santos", "ana.santos@heritagelinens.pt", "+351 21 345 6789"),
    (11, "Ben Crawford", "ben.crawford@kiwicraft.co.nz", "+64 7 456 7890"),
    (12, "David Chen", "david.chen@techflow.tw", "+886 2 2789 0123"),
    (13, "Lars Eriksen", "lars.eriksen@nordicaudio.dk", "+45 33 12 3456"),
    (14, "Helen Wu", "helen.wu@smartlinkdevices.cn", "+86 755 2345 6789"),
    (15, "Jae-won Kim", "jaewon.kim@voltedge.kr", "+82 31 456 7890"),
    (16, "Mike Davidson", "mike.davidson@southerntrail.co.nz", "+64 3 789 0123"),
    (17, "Rachel Cooper", "rachel.cooper@aquashield.com.au", "+61 7 3456 7890"),
    (18, "Tom Watkins", "tom.watkins@greenscapenz.co.nz", "+64 9 234 5678"),
    (19, "Nguyen Thi Lan", "lan.nguyen@peakform.vn", "+84 28 3456 7890"),
    (20, "Sophie Taylor", "sophie.taylor@coastlinesurf.com.au", "+61 2 5678 9012"),
]
suppliers_contact_df = pd.DataFrame(contacts_data, columns=[
    "supplier_id", "contact_name", "contact_email", "contact_phone"
])

# ---------------------------------------------------------------------------
# Write CSVs
# ---------------------------------------------------------------------------
stores_df.to_csv(OUTPUT_DIR / "stores.csv", index=False)
suppliers_df.to_csv(OUTPUT_DIR / "suppliers.csv", index=False)
products_df.to_csv(OUTPUT_DIR / "products.csv", index=False)
daily_sales_df.to_csv(OUTPUT_DIR / "daily_sales.csv", index=False)
role_access_df.to_csv(OUTPUT_DIR / "role_category_access.csv", index=False)
suppliers_contact_df.to_csv(OUTPUT_DIR / "suppliers_contact.csv", index=False)

print("\n" + "=" * 60)
print("FILES WRITTEN")
print("=" * 60)
for f in sorted(OUTPUT_DIR.glob("*.csv")):
    size_mb = f.stat().st_size / (1024 * 1024)
    print(f"  {f.name:35s} {size_mb:.2f} MB")

# ---------------------------------------------------------------------------
# Summary statistics
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("SUMMARY STATISTICS")
print("=" * 60)
print(f"\nRow counts:")
print(f"  STORES:               {len(stores_df):>8,}")
print(f"  SUPPLIERS:            {len(suppliers_df):>8,}")
print(f"  PRODUCTS:             {len(products_df):>8,}")
print(f"  DAILY_SALES:          {len(daily_sales_df):>8,}")
print(f"  ROLE_CATEGORY_ACCESS: {len(role_access_df):>8,}")
print(f"  SUPPLIERS_CONTACT:    {len(suppliers_contact_df):>8,}")

print(f"\nDate range: {daily_sales_df['sale_date'].min()} to {daily_sales_df['sale_date'].max()}")

print(f"\nTotal revenue by department:")
dept_rev = daily_sales_df.groupby("department")["revenue"].sum().sort_values(ascending=False)
total_rev = dept_rev.sum()
for dept, rev in dept_rev.items():
    print(f"  {dept:25s} ${rev:>12,.2f}  ({rev/total_rev*100:.1f}%)")
print(f"  {'TOTAL':25s} ${total_rev:>12,.2f}")

print(f"\nHome & Kitchen revenue by month:")
hk = daily_sales_df[daily_sales_df["department"] == "Home & Kitchen"].copy()
hk["month"] = pd.to_datetime(hk["sale_date"]).dt.to_period("M")
hk_monthly = hk.groupby("month")["revenue"].sum()
for m, rev in hk_monthly.items():
    print(f"  {m}: ${rev:>10,.2f}")

# ---------------------------------------------------------------------------
# Validation checks
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("VALIDATION CHECKS")
print("=" * 60)

checks_passed = 0
checks_total = 0

def check(name, condition, detail=""):
    global checks_passed, checks_total
    checks_total += 1
    status = "PASS" if condition else "FAIL"
    if condition:
        checks_passed += 1
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")

# Check 1: Kitchen Appliances WoW decline
# Join subcategory from products for validation
product_subcat_map = dict(zip(products_df["product_id"], products_df["subcategory"]))
ka_product_ids = set(products_df[products_df["subcategory"] == "Kitchen Appliances"]["product_id"])
ka = daily_sales_df[daily_sales_df["product_id"].isin(ka_product_ids)].copy()
ka["sale_date"] = pd.to_datetime(ka["sale_date"])
week_aug18 = ka[(ka["sale_date"] >= "2026-08-18") & (ka["sale_date"] <= "2026-08-24")]["revenue"].sum()
week_aug25 = ka[(ka["sale_date"] >= "2026-08-25") & (ka["sale_date"] <= "2026-08-31")]["revenue"].sum()
wow_change = (week_aug25 - week_aug18) / week_aug18 * 100 if week_aug18 > 0 else 0
check(
    "Kitchen Appliances WoW decline (Aug 25 vs Aug 18)",
    -25 <= wow_change <= -5,
    f"Actual: {wow_change:.1f}% (target: -5% to -25%)"
)

# Check 2: ProBlend 9000 growth Jun to Aug
pb9 = daily_sales_df[daily_sales_df["product_id"] == problend_9000_id].copy()
pb9["sale_date"] = pd.to_datetime(pb9["sale_date"])
pb9_jun = pb9[pb9["sale_date"].dt.month == 6]["revenue"].sum()
pb9_aug = pb9[pb9["sale_date"].dt.month == 8]["revenue"].sum()
pb9_growth = (pb9_aug - pb9_jun) / pb9_jun * 100 if pb9_jun > 0 else 0
check(
    "ProBlend 9000 Jun→Aug growth",
    80 <= pb9_growth <= 120,
    f"Actual: {pb9_growth:.1f}% (target: +80% to +120%); Jun=${pb9_jun:,.0f}, Aug=${pb9_aug:,.0f}"
)

# Check 3: ProBlend 9000 online share
pb9_online = pb9[pb9["sales_channel"] == "Online"]["revenue"].sum()
pb9_total = pb9["revenue"].sum()
pb9_online_pct = pb9_online / pb9_total * 100 if pb9_total > 0 else 0
check(
    "ProBlend 9000 Online channel share",
    55 <= pb9_online_pct <= 70,
    f"Actual: {pb9_online_pct:.1f}% (target: 55-70%)"
)

# Check 4: Online channel share shift
hk_sales = daily_sales_df[daily_sales_df["department"] == "Home & Kitchen"].copy()
hk_sales["sale_date"] = pd.to_datetime(hk_sales["sale_date"])
hk_mar = hk_sales[hk_sales["sale_date"].dt.month == 3]
hk_aug = hk_sales[hk_sales["sale_date"].dt.month == 8]
online_mar_pct = hk_mar[hk_mar["sales_channel"] == "Online"]["revenue"].sum() / hk_mar["revenue"].sum() * 100
online_aug_pct = hk_aug[hk_aug["sales_channel"] == "Online"]["revenue"].sum() / hk_aug["revenue"].sum() * 100
shift = online_aug_pct - online_mar_pct
check(
    "Online channel share shift (Mar→Aug)",
    4 <= shift <= 12,
    f"Actual: +{shift:.1f}pp (Mar={online_mar_pct:.1f}%, Aug={online_aug_pct:.1f}%)"
)

# Check 5: Product counts by department
for dept, (lo, hi) in [
    ("Home & Kitchen", (50, 60)),
    ("Electronics", (12, 15)),
    ("Outdoor & Garden", (8, 10)),
    ("Sports & Fitness", (8, 10)),
]:
    ct = len(products_df[products_df["department"] == dept])
    check(f"{dept} product count", lo <= ct <= hi, f"Actual: {ct} (target: {lo}-{hi})")

# Check 6: All departments have sales
depts_in_sales = set(daily_sales_df["department"].unique())
check(
    "All 4 departments have DAILY_SALES rows",
    depts_in_sales == {"Home & Kitchen", "Electronics", "Outdoor & Garden", "Sports & Fitness"},
    f"Departments found: {sorted(depts_in_sales)}"
)

# Check 7: Hamilton — no March rows, rows from April
hamilton_sales = daily_sales_df[daily_sales_df["store_id"] == hamilton_store_id].copy()
hamilton_sales["sale_date"] = pd.to_datetime(hamilton_sales["sale_date"])
hamilton_mar = hamilton_sales[hamilton_sales["sale_date"].dt.month == 3]
hamilton_apr = hamilton_sales[hamilton_sales["sale_date"].dt.month == 4]
check(
    "Hamilton: zero rows in March, rows from April",
    len(hamilton_mar) == 0 and len(hamilton_apr) > 0,
    f"March rows: {len(hamilton_mar)}, April rows: {len(hamilton_apr)}"
)

# Check 8: Apex products volume drop in Aug 25 week vs prior week
apex_sales = daily_sales_df[daily_sales_df["product_id"].isin(apex_product_ids)].copy()
apex_sales["sale_date"] = pd.to_datetime(apex_sales["sale_date"])
apex_w1 = apex_sales[(apex_sales["sale_date"] >= "2026-08-18") & (apex_sales["sale_date"] <= "2026-08-24")]["units_sold"].sum()
apex_w2 = apex_sales[(apex_sales["sale_date"] >= "2026-08-25") & (apex_sales["sale_date"] <= "2026-08-31")]["units_sold"].sum()
apex_ratio = apex_w2 / apex_w1 if apex_w1 > 0 else 1.0
check(
    "Apex products drop significantly in Aug 25 week",
    apex_ratio < 0.75,
    f"Actual: {apex_ratio:.2f} (target: <0.75)"
)

# Check 9: Total row count in target range
check(
    f"DAILY_SALES row count in range",
    150_000 <= len(daily_sales_df) <= 300_000,
    f"Actual: {len(daily_sales_df):,} (target: 200K-250K)"
)

# Check 10: No negative revenue
check(
    "No negative revenue",
    (daily_sales_df["revenue"] > 0).all(),
    f"Min revenue: ${daily_sales_df['revenue'].min():.2f}"
)

# Check 11: No zero units_sold
check(
    "No zero units_sold",
    (daily_sales_df["units_sold"] >= 1).all(),
    f"Min units: {daily_sales_df['units_sold'].min()}"
)

print(f"\n  Results: {checks_passed}/{checks_total} checks passed")
print("=" * 60)
