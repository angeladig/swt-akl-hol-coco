"""
Mosaic Retail - Synthetic Dataset Generator
===========================================
Generates the complete dataset for the CoWork HOL at Snowflake World Tour Auckland.

Persona: Jordan Chen, Regional Category Manager (Home & Kitchen, ANZ)
Date range: March 2026 - August 2026 ("today" = Sep 3 2026)

Story beats planted:
1. Kitchen Appliances revenue down ~7% WoW (Apex Kitchen Co supplier delay from Aug 25)
2. Hamilton store outperforming (~25-30% higher growth)
3. Online channel growing faster than in-store (30% -> 38%)
4. ProBlend 9000 premium blender trending up in Jul-Aug
"""

import csv
import random
import os
from datetime import date, timedelta
from pathlib import Path

random.seed(42)

OUTPUT_DIR = Path(__file__).parent
START_DATE = date(2026, 3, 1)
END_DATE = date(2026, 8, 31)  # 184 days

# =============================================================================
# DIMENSION DATA (hand-crafted for narrative control)
# =============================================================================

SUPPLIERS = [
    # id, name, region, avg_lead_days, status
    (1, "Southern Cross Homeware", "NZ", 5, "ACTIVE"),
    (2, "Pacific Cookware Ltd", "NZ", 7, "ACTIVE"),
    (3, "Apex Kitchen Co", "NZ", 10, "DELAYED"),  # Beat 1: delayed supplier
    (4, "Kiwi Textiles Group", "NZ", 4, "ACTIVE"),
    (5, "AusTech Appliances", "AU", 8, "ACTIVE"),
    (6, "CleanPro Industries", "AU", 6, "ACTIVE"),
    (7, "HomeStore Direct", "NZ", 3, "ACTIVE"),
    (8, "BayView Imports", "NZ", 12, "ACTIVE"),
    (9, "GreenLeaf Outdoor", "NZ", 7, "ACTIVE"),
    (10, "TechVibe Electronics", "AU", 9, "ACTIVE"),
    (11, "Summit Sports NZ", "NZ", 5, "ACTIVE"),
    (12, "CoastalLiving AU", "AU", 8, "ACTIVE"),
    (13, "FreshAir Garden Co", "NZ", 6, "ACTIVE"),
    (14, "DigitalEdge Supply", "AU", 10, "ACTIVE"),
    (15, "ActiveGear Ltd", "NZ", 4, "ACTIVE"),
]

STORES = [
    # id, name, city, region, store_type
    (1, "Auckland CBD", "Auckland", "NZ - North Island", "Flagship"),
    (2, "Newmarket", "Auckland", "NZ - North Island", "Standard"),
    (3, "Hamilton Centre", "Hamilton", "NZ - North Island", "Standard"),  # Beat 2: outperformer
    (4, "Wellington Central", "Wellington", "NZ - North Island", "Standard"),
    (5, "Christchurch Mall", "Christchurch", "NZ - South Island", "Standard"),
    (6, "Dunedin South", "Dunedin", "NZ - South Island", "Compact"),
    (7, "Tauranga Bay", "Tauranga", "NZ - North Island", "Compact"),
    (8, "Sydney CBD", "Sydney", "AU - NSW", "Flagship"),
    (9, "Melbourne Central", "Melbourne", "AU - VIC", "Standard"),
    (10, "Brisbane North", "Brisbane", "AU - QLD", "Standard"),
    (11, "Perth City", "Perth", "AU - WA", "Compact"),
    (12, "Online Warehouse", "Auckland", "NZ - North Island", "Online"),
]

# Products: ~150 Home & Kitchen + ~100 other departments
PRODUCTS = []
_pid = 0

def add_products(category, subcategory, items, supplier_id):
    global _pid
    for name, cost, rrp in items:
        _pid += 1
        PRODUCTS.append((_pid, name, category, subcategory, supplier_id, cost, rrp, "ACTIVE"))

# --- HOME AND KITCHEN (Jordan's visible scope) ---

# Kitchen Appliances (supplier 3=Apex for some, 5=AusTech for others)
add_products("Home and Kitchen", "Kitchen Appliances", [
    ("ProBlend 9000", 180.00, 399.00),           # Beat 4: trending product
    ("ProBlend 5000", 90.00, 199.00),
    ("QuickToast Pro", 35.00, 79.99),
    ("QuickToast Lite", 20.00, 49.99),
    ("BrewMaster Drip", 45.00, 99.99),
    ("BrewMaster Espresso", 220.00, 499.00),
    ("FreshPress Juicer", 55.00, 129.00),
    ("AirFry Max 5L", 60.00, 149.00),
    ("AirFry Compact 3L", 40.00, 99.00),
    ("SliceRight Food Processor", 95.00, 219.00),  # Apex supplied
    ("MixMaster Stand Mixer", 150.00, 349.00),     # Apex supplied
    ("MixMaster Hand Mixer", 30.00, 69.99),        # Apex supplied
    ("SteamClean Kettle", 25.00, 59.99),
    ("RapidBoil Kettle 1.7L", 18.00, 44.99),
    ("SmartOven Countertop", 130.00, 299.00),
], 5)

# Override supplier for Apex-supplied products (Beat 1)
# Apex supplies ~30% of Kitchen Appliances by revenue so a 55% drop creates ~7% subcategory dip
APEX_PRODUCTS = ("SliceRight Food Processor", "MixMaster Stand Mixer", "MixMaster Hand Mixer",
                 "AirFry Max 5L", "AirFry Compact 3L")
for i, p in enumerate(PRODUCTS):
    if p[1] in APEX_PRODUCTS:
        PRODUCTS[i] = (p[0], p[1], p[2], p[3], 3, p[5], p[6], p[7])  # supplier_id = 3 (Apex)

add_products("Home and Kitchen", "Cookware", [
    ("CastIron Skillet 28cm", 40.00, 89.99),
    ("NonStick Pan Set (3pc)", 35.00, 79.99),
    ("Stainless Stockpot 8L", 45.00, 109.00),
    ("Ceramic Baking Dish", 15.00, 34.99),
    ("Wok Carbon Steel 32cm", 30.00, 69.99),
    ("Saucepan Set (4pc)", 55.00, 129.00),
    ("Bakeware Set (5pc)", 25.00, 59.99),
    ("Dutch Oven 5L", 60.00, 139.00),
    ("Grill Pan Ribbed", 28.00, 64.99),
    ("Roasting Pan Large", 22.00, 49.99),
], 2)

add_products("Home and Kitchen", "Tableware", [
    ("Porcelain Dinner Set (16pc)", 50.00, 119.00),
    ("Stoneware Mug Set (4)", 12.00, 29.99),
    ("Crystal Wine Glass Set (6)", 35.00, 79.99),
    ("Everyday Tumbler Set (8)", 10.00, 24.99),
    ("Cutlery Set Stainless (24pc)", 30.00, 69.99),
    ("Serving Bowl Bamboo", 8.00, 19.99),
    ("Cheese Board Set", 18.00, 44.99),
    ("Espresso Cup Set (4)", 14.00, 34.99),
], 1)

add_products("Home and Kitchen", "Storage and Organisation", [
    ("Pantry Container Set (10pc)", 20.00, 49.99),
    ("Spice Rack Revolving", 15.00, 36.99),
    ("Under-Shelf Basket (2pk)", 8.00, 19.99),
    ("Vacuum Seal Containers (4pc)", 18.00, 42.99),
    ("Drawer Divider Set", 10.00, 24.99),
    ("Wall-Mount Shelf Floating", 12.00, 29.99),
    ("Lazy Susan Turntable", 9.00, 22.99),
    ("Fridge Organiser Bins (3pc)", 11.00, 27.99),
], 7)

add_products("Home and Kitchen", "Home Textiles", [
    ("Egyptian Cotton Towel Set", 25.00, 59.99),
    ("Waffle Bathmat", 10.00, 24.99),
    ("Linen Cushion Cover (2pk)", 14.00, 34.99),
    ("Microfibre Sheet Set Queen", 22.00, 54.99),
    ("Weighted Blanket 7kg", 40.00, 99.00),
    ("Tea Towel Pack (5)", 6.00, 14.99),
    ("Table Runner Linen", 12.00, 29.99),
    ("Throw Blanket Knit", 18.00, 44.99),
], 4)

add_products("Home and Kitchen", "Cleaning and Laundry", [
    ("CycloneVac Stick Vacuum", 120.00, 279.00),
    ("CycloneVac Handheld", 45.00, 109.00),
    ("SteamMop Pro", 55.00, 129.00),
    ("Robot Vacuum Basic", 150.00, 349.00),
    ("Spin Mop Bucket Set", 18.00, 44.99),
    ("Laundry Basket Foldable", 10.00, 24.99),
    ("Ironing Board Adjustable", 25.00, 59.99),
    ("Drying Rack Tower", 20.00, 49.99),
], 6)

# --- OTHER DEPARTMENTS (hidden by RLS, but exist in data) ---

add_products("Electronics", "Audio", [
    ("WirelessPods Pro", 60.00, 149.00),
    ("OverEar Noise Cancel", 100.00, 249.00),
    ("Bluetooth Speaker Mini", 25.00, 59.99),
    ("Soundbar 2.1", 80.00, 199.00),
    ("Portable DAB Radio", 30.00, 69.99),
], 10)

add_products("Electronics", "Smart Home", [
    ("Smart Plug Pack (3)", 15.00, 39.99),
    ("Video Doorbell Pro", 70.00, 169.00),
    ("Smart Display 8in", 55.00, 129.00),
    ("LED Strip Kit 5m", 12.00, 29.99),
    ("Smart Thermostat", 90.00, 219.00),
], 14)

add_products("Outdoor and Garden", "Garden Tools", [
    ("Cordless Hedge Trimmer", 80.00, 189.00),
    ("Pressure Washer 1800W", 120.00, 279.00),
    ("Garden Hose Reel 30m", 35.00, 84.99),
    ("Pruning Shears Set", 12.00, 29.99),
    ("Wheelbarrow 80L", 45.00, 109.00),
], 13)

add_products("Outdoor and Garden", "Outdoor Furniture", [
    ("Patio Set 4-Seater", 200.00, 499.00),
    ("Hammock Double", 40.00, 99.00),
    ("BBQ Gas 4-Burner", 250.00, 599.00),
    ("Outdoor Cushion Set", 30.00, 74.99),
    ("Sun Umbrella 3m", 50.00, 129.00),
], 9)

add_products("Sports and Fitness", "Gym Equipment", [
    ("Adjustable Dumbbell Set", 90.00, 219.00),
    ("Yoga Mat Premium", 15.00, 39.99),
    ("Resistance Bands (5pk)", 8.00, 19.99),
    ("Exercise Bike Compact", 180.00, 429.00),
    ("Foam Roller 45cm", 10.00, 24.99),
], 11)

add_products("Sports and Fitness", "Activewear", [
    ("Running Shoes Trail", 50.00, 129.00),
    ("Gym Shorts Men", 12.00, 34.99),
    ("Sports Bra High Impact", 15.00, 44.99),
    ("Compression Tights", 18.00, 49.99),
    ("Hiking Backpack 40L", 35.00, 89.99),
], 15)

MEETINGS = [
    (1, "2026-09-01", "09:00", "Weekly Category Standup", "Category team", "Review weekly KPIs and priorities", "Meeting Room 3A"),
    (2, "2026-09-01", "14:00", "Supplier Review - Apex Kitchen Co", "Apex account manager, Procurement", "Discuss delivery delays and resolution timeline", "Meeting Room 2B"),
    (3, "2026-09-02", "10:00", "Q3 Range Planning", "Merchandise Planning team", "Finalise Q4 kitchen range selections", "Board Room"),
    (4, "2026-09-02", "15:30", "Digital Marketing Sync", "Marketing team", "Review online campaign performance for Home & Kitchen", "Virtual - Teams"),
    (5, "2026-09-03", "09:30", "Morning Briefing", "Direct reports", "Daily priorities and blockers", "Meeting Room 3A"),
    (6, "2026-09-03", "14:00", "Buyer Meeting - Q4 Kitchen Range", "Sarah Wong (buyer), Procurement lead", "Present Q4 range recommendations with supporting data", "Board Room"),
    (7, "2026-09-04", "11:00", "Store Visit - Hamilton", "Hamilton store manager", "Review store performance and new layout effectiveness", "Hamilton Centre Store"),
    (8, "2026-09-05", "13:00", "Weekly Wrap / WBR", "Leadership team", "Weekly business review - present category highlights", "Executive Board Room"),
]

# =============================================================================
# SALES DATA GENERATION
# =============================================================================

def day_of_week_factor(d):
    """Weekend boost, midweek dip."""
    dow = d.weekday()  # 0=Mon
    factors = [0.85, 0.80, 0.82, 0.90, 1.10, 1.30, 1.20]
    return factors[dow]

def monthly_trend(d):
    """Slight upward trend over 6 months."""
    months_elapsed = (d.year - START_DATE.year) * 12 + (d.month - START_DATE.month)
    return 1.0 + (months_elapsed * 0.02)  # +2% per month

def online_share(d):
    """Online share grows from 30% to 38% over the period."""
    days_elapsed = (d - START_DATE).days
    total_days = (END_DATE - START_DATE).days
    return 0.30 + 0.08 * (days_elapsed / total_days)

def hamilton_boost(d, store_id, product_id=None):
    """Hamilton (store 3) ramps up from April — with extra ProBlend uplift."""
    if store_id != 3:
        return 1.0
    if d < date(2026, 4, 1):
        return 0.95  # slightly below average before renovation
    months_since_open = (d.year - 2026) * 12 + (d.month - 4)
    base_boost = 1.05 + (months_since_open * 0.02)  # grows to ~1.15x by August

    # ProBlend products (id 1 = ProBlend 9000, id 2 = ProBlend 5000) get extra
    # Hamilton uplift — simulates store manager pushing the range harder after
    # early success, relevant to the buyer meeting narrative
    if product_id in (1, 2) and d >= date(2026, 6, 1):
        weeks_in = (d - date(2026, 6, 1)).days / 7
        problend_extra = 1.1 + (weeks_in * 0.008)  # ~+20% by end Aug on top of base
        return base_boost * problend_extra

    return base_boost

def apex_supplier_dip(d, supplier_id):
    """Apex (supplier 3) products drop from Aug 25 onwards."""
    if supplier_id != 3:
        return 1.0
    if d >= date(2026, 8, 25):
        return 0.55  # ~45% reduction in Apex products
    return 1.0

def problend_surge(d, product_id):
    """ProBlend 9000 (product 1) surges in Jul-Aug."""
    if product_id != 1:
        return 1.0
    if d >= date(2026, 7, 1):
        weeks_in = (d - date(2026, 7, 1)).days / 7
        return 1.2 + (weeks_in * 0.03)  # moderate accelerating growth
    return 1.0

def base_daily_quantity(product, store):
    """Base units/day varies by product price and store type."""
    rrp = product[6]
    store_type = store[4]

    # Higher-priced items sell fewer units
    if rrp >= 300:
        base = 1.2
    elif rrp >= 150:
        base = 2.5
    elif rrp >= 80:
        base = 4.0
    elif rrp >= 40:
        base = 6.0
    else:
        base = 10.0

    # Store type multiplier
    type_mult = {"Flagship": 1.8, "Standard": 1.0, "Compact": 0.6, "Online": 0.0}
    return base * type_mult.get(store_type, 1.0)


def generate_sales():
    """Generate daily sales records."""
    sales = []
    sale_id = 0
    current = START_DATE

    # Calculate total in-store capacity to calibrate online volume
    # We want online to be ~30-38% of total, so online_vol = instore_vol * (pct / (1-pct))
    # Average across all physical stores (excl online warehouse)
    physical_stores = [s for s in STORES if s[4] != "Online"]
    num_physical = len(physical_stores)

    while current <= END_DATE:
        day_factor = day_of_week_factor(current)
        trend = monthly_trend(current)
        online_pct = online_share(current)

        for product in PRODUCTS:
            pid = product[0]
            category = product[2]
            supplier_id = product[4]
            rrp = product[6]

            instore_total_qty = 0

            # Generate in-store sales per physical store
            for store in physical_stores:
                sid = store[0]

                base_qty = base_daily_quantity(product, store)
                if base_qty == 0:
                    continue

                qty = base_qty * day_factor * trend
                qty *= hamilton_boost(current, sid, pid)
                qty *= apex_supplier_dip(current, supplier_id)
                qty *= problend_surge(current, pid)

                qty *= random.uniform(0.7, 1.3)
                qty = max(0, round(qty))
                instore_total_qty += qty

                if qty > 0:
                    discount_pct = random.choices([0, 0.05, 0.10, 0.15], weights=[70, 15, 10, 5])[0]
                    revenue = round(qty * rrp * (1 - discount_pct), 2)
                    discount_amt = round(qty * rrp * discount_pct, 2)

                    sale_id += 1
                    sales.append((sale_id, str(current), pid, sid, "In-Store", qty, revenue, discount_amt, category))

            # Online sales: calibrated to achieve target online_pct of total
            # online_qty / (online_qty + instore_qty) = online_pct
            # => online_qty = instore_qty * online_pct / (1 - online_pct)
            # Note: apex_supplier_dip and problend_surge are already in instore_total_qty
            if instore_total_qty > 0:
                online_qty = instore_total_qty * (online_pct / (1 - online_pct))

                # ProBlend 9000 extra strong online
                if pid == 1 and current >= date(2026, 7, 1):
                    online_qty *= 1.3

                online_qty *= random.uniform(0.75, 1.25)
                online_qty = max(0, round(online_qty))

                if online_qty > 0:
                    discount_pct = random.choices([0, 0.05, 0.10, 0.15], weights=[65, 18, 12, 5])[0]
                    revenue = round(online_qty * rrp * (1 - discount_pct), 2)
                    discount_amt = round(online_qty * rrp * discount_pct, 2)

                    sale_id += 1
                    sales.append((sale_id, str(current), pid, 12, "Online", online_qty, revenue, discount_amt, category))

        current += timedelta(days=1)

    return sales


# =============================================================================
# OUTPUT GENERATION
# =============================================================================

def write_csv(filename, headers, rows):
    filepath = OUTPUT_DIR / filename
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"  Written {filepath.name}: {len(rows)} rows")

def main():
    print("Generating Mosaic Retail dataset...")
    print(f"  Date range: {START_DATE} to {END_DATE}")
    print(f"  Products: {len(PRODUCTS)} ({sum(1 for p in PRODUCTS if p[2] == 'Home and Kitchen')} Home & Kitchen)")
    print()

    # Write dimension CSVs
    write_csv("suppliers.csv",
              ["supplier_id", "supplier_name", "region", "avg_lead_days", "status"],
              SUPPLIERS)

    write_csv("stores.csv",
              ["store_id", "store_name", "city", "region", "store_type"],
              STORES)

    write_csv("products.csv",
              ["product_id", "product_name", "category", "subcategory", "supplier_id", "unit_cost", "rrp", "status"],
              PRODUCTS)

    write_csv("meetings.csv",
              ["meeting_id", "meeting_date", "meeting_time", "title", "attendees", "notes", "location"],
              MEETINGS)

    # Generate and write sales
    print("\n  Generating daily sales (this may take a moment)...")
    sales = generate_sales()
    write_csv("daily_sales.csv",
              ["sale_id", "sale_date", "product_id", "store_id", "channel", "quantity", "revenue", "discount_amount", "category"],
              sales)

    print(f"\n  Total sales records: {len(sales)}")
    print(f"  Home & Kitchen sales: {sum(1 for s in sales if s[8] == 'Home and Kitchen')}")
    print(f"  Other department sales: {sum(1 for s in sales if s[8] != 'Home and Kitchen')}")
    print("\nDone!")


if __name__ == "__main__":
    main()
