-- =============================================================================
-- Mosaic Retail - CoWork HOL Setup Script
-- Snowflake World Tour Auckland 2026
-- =============================================================================
-- Run this script as ACCOUNTADMIN in each trial account to provision the
-- complete CoWork hands-on lab environment.
--
-- Pre-requisite: The 5 CSV files (daily_sales.csv, products.csv, stores.csv,
-- suppliers.csv, meetings.csv) must be available to load. See Section 6 for
-- staging options.
-- =============================================================================

USE ROLE ACCOUNTADMIN;

-- =============================================================================
-- 1. ACCOUNT-LEVEL SETTINGS
-- =============================================================================

-- Enable cross-region inference (required for Cortex model availability)
ALTER ACCOUNT SET CORTEX_ENABLED_CROSS_REGION = 'ANY_REGION';

-- =============================================================================
-- 2. WAREHOUSE
-- =============================================================================

CREATE WAREHOUSE IF NOT EXISTS HOL_WH
    WAREHOUSE_SIZE = 'XSMALL'
    AUTO_SUSPEND = 60
    AUTO_RESUME = TRUE
    COMMENT = 'Warehouse for CoWork HOL queries';

USE WAREHOUSE HOL_WH;

-- =============================================================================
-- 3. DATABASE AND SCHEMA
-- =============================================================================

CREATE DATABASE IF NOT EXISTS MOSAIC_RETAIL
    COMMENT = 'Mosaic Retail - Omnichannel retailer (ANZ) for CoWork HOL';

USE DATABASE MOSAIC_RETAIL;
CREATE SCHEMA IF NOT EXISTS RETAIL
    COMMENT = 'Core retail data - sales, products, stores, suppliers';
USE SCHEMA RETAIL;

-- =============================================================================
-- 4. TABLES
-- =============================================================================

CREATE OR REPLACE TABLE SUPPLIERS (
    supplier_id INT PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL,
    region VARCHAR(10) NOT NULL,
    avg_lead_days INT,
    status VARCHAR(20) DEFAULT 'ACTIVE'
);

CREATE OR REPLACE TABLE PRODUCTS (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(200) NOT NULL,
    category VARCHAR(50) NOT NULL,
    subcategory VARCHAR(50) NOT NULL,
    supplier_id INT REFERENCES SUPPLIERS(supplier_id),
    unit_cost NUMBER(10,2),
    rrp NUMBER(10,2),
    status VARCHAR(20) DEFAULT 'ACTIVE'
);

CREATE OR REPLACE TABLE STORES (
    store_id INT PRIMARY KEY,
    store_name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    region VARCHAR(50) NOT NULL,
    store_type VARCHAR(20) NOT NULL
);

CREATE OR REPLACE TABLE DAILY_SALES (
    sale_id INT PRIMARY KEY,
    sale_date DATE NOT NULL,
    product_id INT REFERENCES PRODUCTS(product_id),
    store_id INT REFERENCES STORES(store_id),
    channel VARCHAR(20) NOT NULL,
    quantity INT NOT NULL,
    revenue NUMBER(12,2) NOT NULL,
    discount_amount NUMBER(12,2) DEFAULT 0,
    category VARCHAR(50) NOT NULL
);

CREATE OR REPLACE TABLE MEETINGS (
    meeting_id INT PRIMARY KEY,
    meeting_date DATE NOT NULL,
    meeting_time VARCHAR(10) NOT NULL,
    title VARCHAR(200) NOT NULL,
    attendees VARCHAR(500),
    notes VARCHAR(1000),
    location VARCHAR(200)
);

CREATE OR REPLACE TABLE ROLE_CATEGORY_ACCESS (
    role_name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL
);

-- =============================================================================
-- 5. LOAD DIMENSION DATA (small tables - inline INSERT)
-- =============================================================================

INSERT INTO SUPPLIERS VALUES
(1, 'Southern Cross Homeware', 'NZ', 5, 'ACTIVE'),
(2, 'Pacific Cookware Ltd', 'NZ', 7, 'ACTIVE'),
(3, 'Apex Kitchen Co', 'NZ', 10, 'DELAYED'),
(4, 'Kiwi Textiles Group', 'NZ', 4, 'ACTIVE'),
(5, 'AusTech Appliances', 'AU', 8, 'ACTIVE'),
(6, 'CleanPro Industries', 'AU', 6, 'ACTIVE'),
(7, 'HomeStore Direct', 'NZ', 3, 'ACTIVE'),
(8, 'BayView Imports', 'NZ', 12, 'ACTIVE'),
(9, 'GreenLeaf Outdoor', 'NZ', 7, 'ACTIVE'),
(10, 'TechVibe Electronics', 'AU', 9, 'ACTIVE'),
(11, 'Summit Sports NZ', 'NZ', 5, 'ACTIVE'),
(12, 'CoastalLiving AU', 'AU', 8, 'ACTIVE'),
(13, 'FreshAir Garden Co', 'NZ', 6, 'ACTIVE'),
(14, 'DigitalEdge Supply', 'AU', 10, 'ACTIVE'),
(15, 'ActiveGear Ltd', 'NZ', 4, 'ACTIVE');

INSERT INTO STORES VALUES
(1, 'Auckland CBD', 'Auckland', 'NZ - North Island', 'Flagship'),
(2, 'Newmarket', 'Auckland', 'NZ - North Island', 'Standard'),
(3, 'Hamilton Centre', 'Hamilton', 'NZ - North Island', 'Standard'),
(4, 'Wellington Central', 'Wellington', 'NZ - North Island', 'Standard'),
(5, 'Christchurch Mall', 'Christchurch', 'NZ - South Island', 'Standard'),
(6, 'Dunedin South', 'Dunedin', 'NZ - South Island', 'Compact'),
(7, 'Tauranga Bay', 'Tauranga', 'NZ - North Island', 'Compact'),
(8, 'Sydney CBD', 'Sydney', 'AU - NSW', 'Flagship'),
(9, 'Melbourne Central', 'Melbourne', 'AU - VIC', 'Standard'),
(10, 'Brisbane North', 'Brisbane', 'AU - QLD', 'Standard'),
(11, 'Perth City', 'Perth', 'AU - WA', 'Compact'),
(12, 'Online Warehouse', 'Auckland', 'NZ - North Island', 'Online');

INSERT INTO MEETINGS VALUES
(1, '2026-09-01', '09:00', 'Weekly Category Standup', 'Category team', 'Review weekly KPIs and priorities', 'Meeting Room 3A'),
(2, '2026-09-01', '14:00', 'Supplier Review - Apex Kitchen Co', 'Apex account manager, Procurement', 'Discuss delivery delays and resolution timeline', 'Meeting Room 2B'),
(3, '2026-09-02', '10:00', 'Q3 Range Planning', 'Merchandise Planning team', 'Finalise Q4 kitchen range selections', 'Board Room'),
(4, '2026-09-02', '15:30', 'Digital Marketing Sync', 'Marketing team', 'Review online campaign performance for Home and Kitchen', 'Virtual - Teams'),
(5, '2026-09-03', '09:30', 'Morning Briefing', 'Direct reports', 'Daily priorities and blockers', 'Meeting Room 3A'),
(6, '2026-09-03', '14:00', 'Buyer Meeting - Q4 Kitchen Range', 'Sarah Wong (buyer), Procurement lead', 'Present Q4 range recommendations with supporting data', 'Board Room'),
(7, '2026-09-04', '11:00', 'Store Visit - Hamilton', 'Hamilton store manager', 'Review store performance and new layout effectiveness', 'Hamilton Centre Store'),
(8, '2026-09-05', '13:00', 'Weekly Wrap / WBR', 'Leadership team', 'Weekly business review - present category highlights', 'Executive Board Room');

-- RLS mapping: attendee role only sees Home and Kitchen
INSERT INTO ROLE_CATEGORY_ACCESS VALUES
('HOL_ATTENDEE_ROLE', 'Home and Kitchen');

-- =============================================================================
-- 6. FILE FORMAT AND STAGE
-- =============================================================================

CREATE OR REPLACE FILE FORMAT CSV_FORMAT
    TYPE = 'CSV'
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    SKIP_HEADER = 1
    NULL_IF = ('NULL', '');

CREATE OR REPLACE STAGE HOL_DATA_STAGE
    FILE_FORMAT = CSV_FORMAT;

-- =============================================================================
-- 7. LOAD PRODUCTS AND DAILY SALES FROM STAGE
-- =============================================================================
-- Option A: PUT files from local machine (for testing)
--   PUT file:///path/to/products.csv @HOL_DATA_STAGE AUTO_COMPRESS=TRUE;
--   PUT file:///path/to/daily_sales.csv @HOL_DATA_STAGE AUTO_COMPRESS=TRUE;
--
-- Option B: Copy from an external stage / S3 bucket (for bulk provisioning)
--   COPY INTO PRODUCTS FROM @EXTERNAL_STAGE/products.csv.gz FILE_FORMAT = CSV_FORMAT;
--   COPY INTO DAILY_SALES FROM @EXTERNAL_STAGE/daily_sales.csv.gz FILE_FORMAT = CSV_FORMAT;
--
-- Option C: Cross-account data share from a master HOL account (cleanest)
--   -- No stage needed; tables come pre-populated from the share

COPY INTO PRODUCTS FROM @HOL_DATA_STAGE/products.csv.gz FILE_FORMAT = CSV_FORMAT;
COPY INTO DAILY_SALES FROM @HOL_DATA_STAGE/daily_sales.csv.gz FILE_FORMAT = CSV_FORMAT;

-- =============================================================================
-- 8. ROLES
-- =============================================================================

CREATE ROLE IF NOT EXISTS HOL_ATTENDEE_ROLE
    COMMENT = 'Role for CoWork HOL attendees - restricted to Home and Kitchen data';
CREATE ROLE IF NOT EXISTS HOL_ADMIN_ROLE
    COMMENT = 'Admin role for HOL - can see all departments';

GRANT ROLE HOL_ATTENDEE_ROLE TO ROLE ACCOUNTADMIN;
GRANT ROLE HOL_ADMIN_ROLE TO ROLE ACCOUNTADMIN;

-- =============================================================================
-- 9. ROW-LEVEL SECURITY
-- =============================================================================

CREATE OR REPLACE ROW ACCESS POLICY CATEGORY_RLS AS (category_val VARCHAR)
RETURNS BOOLEAN ->
    CURRENT_ROLE() = 'HOL_ADMIN_ROLE'
    OR CURRENT_ROLE() = 'ACCOUNTADMIN'
    OR EXISTS (
        SELECT 1
        FROM MOSAIC_RETAIL.RETAIL.ROLE_CATEGORY_ACCESS
        WHERE role_name = CURRENT_ROLE()
          AND department = category_val
    );

ALTER TABLE DAILY_SALES ADD ROW ACCESS POLICY CATEGORY_RLS ON (category);
ALTER TABLE PRODUCTS ADD ROW ACCESS POLICY CATEGORY_RLS ON (category);

-- =============================================================================
-- 10. SEMANTIC VIEW
-- =============================================================================

CALL SYSTEM$CREATE_SEMANTIC_VIEW_FROM_YAML('MOSAIC_RETAIL.RETAIL.MOSAIC_RETAIL_ANALYTICS', $$
tables:
  - name: daily_sales
    base_table:
      database: MOSAIC_RETAIL
      schema: RETAIL
      table: DAILY_SALES
    primary_key: [SALE_ID]
    comment: "Daily aggregated sales transactions by product, store, and channel."
    facts:
      - name: revenue
        comment: "Revenue from the sale in NZD."
      - name: quantity
        comment: "Number of units sold."
      - name: discount_amount
        comment: "Discount given in NZD."
    dimensions:
      - name: sale_date
        synonyms: [date, day]
        comment: "The date the sale occurred."
      - name: channel
        synonyms: [sales channel]
        comment: "Sales channel - either Online or In-Store."
      - name: category
        comment: "Product department/category."
      - name: product_id
      - name: store_id
    metrics:
      - name: total_revenue
        expression: SUM(daily_sales.revenue)
        synonyms: [sales, total sales, income]
        comment: "Sum of all revenue in NZD."
      - name: total_quantity
        expression: SUM(daily_sales.quantity)
        synonyms: [units sold, volume]
        comment: "Total number of units sold."
      - name: total_discount
        expression: SUM(daily_sales.discount_amount)
        synonyms: [discounts, markdowns]
        comment: "Total discount given in NZD."

  - name: products
    base_table:
      database: MOSAIC_RETAIL
      schema: RETAIL
      table: PRODUCTS
    primary_key: [PRODUCT_ID]
    comment: "Product catalog with categories, pricing, and supplier information."
    facts:
      - name: unit_cost
        comment: "Wholesale cost per unit in NZD."
      - name: rrp
        synonyms: [price, retail price]
        comment: "Recommended retail price in NZD."
    dimensions:
      - name: product_id
      - name: product_name
        synonyms: [product, item]
        comment: "Name of the product."
      - name: subcategory
        synonyms: [sub-category, product type, product group]
        comment: "Product subcategory (e.g. Kitchen Appliances, Cookware)."
      - name: product_category
        expr: category
        comment: "Top-level product department."
      - name: product_status
        expr: status
        comment: "Product status (ACTIVE or DISCONTINUED)."
      - name: supplier_id

  - name: stores
    base_table:
      database: MOSAIC_RETAIL
      schema: RETAIL
      table: STORES
    primary_key: [STORE_ID]
    comment: "Retail store locations across ANZ."
    dimensions:
      - name: store_id
      - name: store_name
        synonyms: [store, location, branch]
        comment: "Name of the store location."
      - name: city
        comment: "City where the store is located."
      - name: region
        comment: "Geographic region (e.g. NZ - North Island, AU - NSW)."
      - name: store_type
        comment: "Store format - Flagship, Standard, Compact, or Online."

  - name: suppliers
    base_table:
      database: MOSAIC_RETAIL
      schema: RETAIL
      table: SUPPLIERS
    primary_key: [SUPPLIER_ID]
    comment: "Supplier directory with lead times and delivery status."
    facts:
      - name: avg_lead_days
        synonyms: [lead time, delivery days]
        comment: "Average delivery lead time in days."
    dimensions:
      - name: supplier_id
      - name: supplier_name
        synonyms: [supplier, vendor]
        comment: "Name of the supplier company."
      - name: supplier_region
        expr: region
        comment: "Country where the supplier is based (NZ or AU)."
      - name: supplier_status
        expr: status
        synonyms: [delivery status]
        comment: "Current supplier status - ACTIVE or DELAYED."

  - name: meetings
    base_table:
      database: MOSAIC_RETAIL
      schema: RETAIL
      table: MEETINGS
    primary_key: [MEETING_ID]
    comment: "Calendar and meeting schedule. Use this table when the user asks about their schedule, calendar, meetings, or what is on today."
    dimensions:
      - name: meeting_date
        synonyms: [date, when]
        comment: "The date of the meeting."
      - name: meeting_time
        synonyms: [time, start time]
        comment: "The start time of the meeting (e.g. 09:00, 14:00)."
      - name: title
        synonyms: [meeting name, subject, event]
        comment: "Title or subject of the meeting."
      - name: attendees
        synonyms: [participants, who]
        comment: "People attending the meeting."
      - name: notes
        comment: "Meeting agenda or preparation notes."
      - name: location
        comment: "Where the meeting takes place."

relationships:
  - name: sales_to_products
    left_table: daily_sales
    left_columns: [product_id]
    right_table: products
    right_columns: [product_id]
    relationship_type: many_to_one
  - name: sales_to_stores
    left_table: daily_sales
    left_columns: [store_id]
    right_table: stores
    right_columns: [store_id]
    relationship_type: many_to_one
  - name: products_to_suppliers
    left_table: products
    left_columns: [supplier_id]
    right_table: suppliers
    right_columns: [supplier_id]
    relationship_type: many_to_one

module_custom_instructions: |
  The dataset contains sales data through August 31, 2026. Today is 2026-09-03.
  When the user says "last week", use 2026-08-25 to 2026-08-31.
  When the user says "this month" or "current month", use August 2026.
  When the user says "last month", use July 2026.
  When the user asks about their calendar, schedule, or meetings for "today", query the meetings table with meeting_date = '2026-09-03'.
  All currency is in NZD. Round numeric values to 2 decimal places.

verified_queries:
  - name: whats_on_today
    question: "What is on my calendar today?"
    use_as_onboarding_question: true
    verified_at: 1724976000
    verified_by: "Angela Dignadice"
    sql: |
      SELECT MEETING_TIME, TITLE, ATTENDEES, NOTES, LOCATION
      FROM MOSAIC_RETAIL.RETAIL.MEETINGS
      WHERE MEETING_DATE = '2026-09-03'
      ORDER BY MEETING_TIME

  - name: kitchen_appliances_last_week
    question: "How did Kitchen Appliances perform last week?"
    verified_at: 1724976000
    verified_by: "Angela Dignadice"
    sql: |
      SELECT p.SUBCATEGORY, ROUND(SUM(s.REVENUE), 2) AS total_revenue, SUM(s.QUANTITY) AS total_units
      FROM MOSAIC_RETAIL.RETAIL.DAILY_SALES s
      JOIN MOSAIC_RETAIL.RETAIL.PRODUCTS p ON s.PRODUCT_ID = p.PRODUCT_ID
      WHERE p.SUBCATEGORY = 'Kitchen Appliances'
        AND s.SALE_DATE BETWEEN '2026-08-25' AND '2026-08-31'
      GROUP BY p.SUBCATEGORY

  - name: best_performing_store
    question: "Which store is performing best?"
    verified_at: 1724976000
    verified_by: "Angela Dignadice"
    sql: |
      SELECT st.STORE_NAME, st.CITY, ROUND(SUM(s.REVENUE), 2) AS total_revenue
      FROM MOSAIC_RETAIL.RETAIL.DAILY_SALES s
      JOIN MOSAIC_RETAIL.RETAIL.STORES st ON s.STORE_ID = st.STORE_ID
      WHERE s.SALE_DATE BETWEEN '2026-08-01' AND '2026-08-31'
      GROUP BY st.STORE_NAME, st.CITY
      ORDER BY total_revenue DESC
      LIMIT 10

  - name: online_vs_instore_trend
    question: "How is online vs in-store trending?"
    verified_at: 1724976000
    verified_by: "Angela Dignadice"
    sql: |
      SELECT DATE_TRUNC('month', s.SALE_DATE) AS month, s.CHANNEL, ROUND(SUM(s.REVENUE), 2) AS total_revenue
      FROM MOSAIC_RETAIL.RETAIL.DAILY_SALES s
      WHERE s.SALE_DATE >= '2026-03-01'
      GROUP BY DATE_TRUNC('month', s.SALE_DATE), s.CHANNEL
      ORDER BY month, s.CHANNEL

  - name: supplier_status
    question: "Are there any supplier issues?"
    verified_at: 1724976000
    verified_by: "Angela Dignadice"
    sql: |
      SELECT sup.SUPPLIER_NAME, sup.STATUS, sup.AVG_LEAD_DAYS, COUNT(DISTINCT p.PRODUCT_ID) AS products_affected
      FROM MOSAIC_RETAIL.RETAIL.SUPPLIERS sup
      JOIN MOSAIC_RETAIL.RETAIL.PRODUCTS p ON sup.SUPPLIER_ID = p.SUPPLIER_ID
      WHERE sup.STATUS != 'ACTIVE'
      GROUP BY sup.SUPPLIER_NAME, sup.STATUS, sup.AVG_LEAD_DAYS
$$);

-- =============================================================================
-- 11. CORTEX AGENT
-- =============================================================================

CREATE OR REPLACE CORTEX AGENT MOSAIC_RETAIL.RETAIL.MOSAIC_RETAIL_AGENT
    COMMENT = 'CoWork agent for Mosaic Retail HOL - Auckland World Tour'
    FROM SPECIFICATION $$
models:
  orchestration: "auto"
orchestration:
  budget:
    seconds: 30
instructions:
  response: |
    You are a retail analytics assistant for Mosaic Retail, an omnichannel
    retailer operating across Australia and New Zealand.

    Your expertise covers sales performance, product trends, store comparisons,
    channel mix (Online vs In-Store), supplier health, and schedule management.

    Response guidelines:
    - Be concise and business-oriented. Lead with the insight, then supporting data.
    - Use NZD for all currency values.
    - When showing time-based data, prefer line or bar chart visualizations.
    - When comparing categories or stores, use bar charts or tables.
    - If a question is ambiguous, ask a brief clarifying question.
    - Today's date is 2026-09-03.
  orchestration: |
    Use the retail_analytics tool for ALL questions including:
    - Sales, revenue, products, stores, suppliers, performance metrics
    - Schedule, calendar, meetings, what is on today
    Use data_to_chart when presenting time-series or comparison data.
tools:
  - tool_spec:
      type: "cortex_analyst_text_to_sql"
      name: "retail_analytics"
      description: "Queries Mosaic Retail data including sales performance, products, stores, suppliers, AND the meetings/calendar schedule. Use this for ANY data question including schedule and calendar queries."
  - tool_spec:
      type: "data_to_chart"
      name: "data_to_chart"
      description: "Generates chart visualizations from query results"
tool_resources:
  retail_analytics:
    semantic_view: "MOSAIC_RETAIL.RETAIL.MOSAIC_RETAIL_ANALYTICS"
    execution_environment:
      type: "warehouse"
      warehouse: "HOL_WH"
$$;

-- =============================================================================
-- 12. GRANTS
-- =============================================================================

GRANT USAGE ON WAREHOUSE HOL_WH TO ROLE HOL_ATTENDEE_ROLE;
GRANT USAGE ON DATABASE MOSAIC_RETAIL TO ROLE HOL_ATTENDEE_ROLE;
GRANT USAGE ON SCHEMA MOSAIC_RETAIL.RETAIL TO ROLE HOL_ATTENDEE_ROLE;
GRANT SELECT ON ALL TABLES IN SCHEMA MOSAIC_RETAIL.RETAIL TO ROLE HOL_ATTENDEE_ROLE;
GRANT USAGE ON SEMANTIC VIEW MOSAIC_RETAIL.RETAIL.MOSAIC_RETAIL_ANALYTICS TO ROLE HOL_ATTENDEE_ROLE;
GRANT USAGE ON CORTEX AGENT MOSAIC_RETAIL.RETAIL.MOSAIC_RETAIL_AGENT TO ROLE HOL_ATTENDEE_ROLE;

-- =============================================================================
-- 13. PROVISION ATTENDEE USER
-- =============================================================================
-- For each attendee user, run the following (or use the stored procedure below).
-- Replace 'ATTENDEE' with the actual username created by the provisioning system.

-- GRANT ROLE HOL_ATTENDEE_ROLE TO USER ATTENDEE;
-- ALTER USER ATTENDEE SET DEFAULT_ROLE = 'HOL_ATTENDEE_ROLE';
-- ALTER USER ATTENDEE SET DEFAULT_WAREHOUSE = 'HOL_WH';
-- ALTER USER ATTENDEE SET DEFAULT_NAMESPACE = 'MOSAIC_RETAIL.RETAIL';

CREATE OR REPLACE PROCEDURE MOSAIC_RETAIL.RETAIL.PROVISION_ATTENDEE(username VARCHAR)
RETURNS VARCHAR
LANGUAGE SQL
EXECUTE AS CALLER
AS
BEGIN
    EXECUTE IMMEDIATE 'GRANT ROLE HOL_ATTENDEE_ROLE TO USER ' || :username;
    EXECUTE IMMEDIATE 'ALTER USER ' || :username || ' SET DEFAULT_ROLE = ''HOL_ATTENDEE_ROLE''';
    EXECUTE IMMEDIATE 'ALTER USER ' || :username || ' SET DEFAULT_WAREHOUSE = ''HOL_WH''';
    EXECUTE IMMEDIATE 'ALTER USER ' || :username || ' SET DEFAULT_NAMESPACE = ''MOSAIC_RETAIL.RETAIL''';
    RETURN 'User ' || :username || ' configured successfully';
END;

-- Example usage:
-- CALL MOSAIC_RETAIL.RETAIL.PROVISION_ATTENDEE('USER_001');

-- =============================================================================
-- SETUP COMPLETE
-- =============================================================================
-- After running this script, the attendee can:
-- 1. Open CoWork (Snowflake Intelligence)
-- 2. Select the MOSAIC_RETAIL_AGENT
-- 3. Start prompting: "What's on my calendar today?"
-- =============================================================================
