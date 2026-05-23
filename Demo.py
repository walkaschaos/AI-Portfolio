import streamlit as st
import time
import streamlit.components.v1 as components

# --- PAGE CONFIG ---
st.set_page_config(page_title="Sacha Laskow | AI-Driven CS Ops", layout="wide", initial_sidebar_state="expanded")

# --- CUSTOM CSS FOR 'DARK MODE / ENTERPRISE' VIBE ---
st.markdown("""
    <style>
    .main {background-color: #0E1117;}
    h1, h2, h3 {color: #FAFAFA;}
    .stButton>button {background-color: #2E86C1; color: white; border-radius: 5px; width: 100%;}
    .stButton>button:hover {background-color: #1B4F72;}
    .metric-card {background-color: #1E2129; padding: 20px; border-radius: 10px; border-left: 5px solid #2E86C1;}
   
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
try:
    # Add your profile picture and scale it to fit the sidebar
    st.sidebar.image("Sacha_Headshot.png", use_container_width=True)
except Exception:
    # If the picture isn't uploaded yet, silently skip it without crashing
    pass

st.sidebar.title("Sacha Laskow")
st.sidebar.markdown("**CS Ops & Strategy Leader**")
st.sidebar.divider()
st.sidebar.markdown("Select a module to explore the architecture.")
playbook = st.sidebar.radio("Navigation", [
    "Executive Portfolio & Resume", 
    "1. Predictive Health Score", 
    "2. Automated QBR Generator", 
    "3. Contextual Release Notes", 
    "4. Early Warning Adoption", 
    "5. C360 Account Summary"
])

# --- EXECUTIVE PORTFOLIO & RESUME ---
if playbook == "Executive Portfolio & Resume":
    st.title("Architecting Scalable Success in the Age of AI")
    st.markdown("### Customer Success isn’t just a function—it’s a growth engine.")
    st.write("I build the strategy, tooling & data architecture, and enablement programs that allow enterprise teams to scale smarter. I blend data, automation, and AI to remove friction so CSMs can focus on what matters: driving adoption, expansion, and retention.")
    st.divider()

    tab1, tab2 = st.tabs(["Resume & Experience", "Strategy Playbook"])

    with tab1:
        st.subheader("Customer Success Strategy & Ops Leader")
        
        # Resume Download Logic
        try:
            with open("Sacha_Laskow_Resume_2026.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()
            st.download_button(
                label="📥 Download Full Resume (PDF)",
                data=PDFbyte,
                file_name="Sacha_Laskow_Resume_2026.pdf",
                mime="application/octet-stream"
            )
        except FileNotFoundError:
            st.warning("Resume PDF not found. (Note to self: Upload 'Sacha_Laskow_Resume.pdf' to the GitHub repository).")
            
        st.markdown("---")
        st.markdown("### Customer Success Operations Manager • Spare")
        st.markdown("*April 2026 – Present*")
        st.markdown("""
        * **Architected a new CS Segmentation model** to execute a new Scaled Success motion, automating legacy workflows to instantly free up 15+ hours per week per strategic CSM for high-value engagements.
        * **Partnered with Forward Deployed Engineering** to launch an AI-driven C360 Customer Health dashboard, empowering the CS team with advanced adoption, expansion and churn risk telemetry.
        * **Secured executive sponsorship** to overhaul post-sales infrastructure, bridging technical tooling with GTM strategy to drive seamless change management.
        """)

        st.markdown("### Senior Manager, CS Ops & Strategy • Boomi")
        st.markdown("*August 2022 – April 2026*")
        st.markdown("""
        * **Led enterprise Gainsight architecture and CS strategy**, driving a 50% YoY increase in expansion pipeline and a 30% YoY increase in expansion ARR.
        * **Directed AI-driven retention initiatives**, deploying machine learning churn models (Reef.AI, Staircase.AI) that surfaced risk signals with 80% accuracy up to 6 months in advance.
        * **Automated digital onboarding and adoption nurtures**, decreasing CSM manual workload by 8–10 hours per week while boosting quarterly product adoption by 20%.
        """)

    with tab2:
        st.subheader("The AI-Driven Operations Playbook")
        st.write("My framework for transitioning teams from reactive check-ins to predictive defense.")
        
        # Embedded Gamma Site
        components.iframe("https://architecting-scalable-cs-41xuyqd.gamma.site/", height=750, scrolling=True)

# --- PLAYBOOK 1: PREDICTIVE HEALTH SCORE ---
elif playbook == "1. Predictive Health Score":
    st.title("Predictive AI Health Score")
    st.markdown("Moving from reactive lagging indicators to proactive sentiment analysis.")
    st.divider()
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("LLM Sentiment Ingestion Engine")
        sentiment = st.slider("Simulate average tone across Support Tickets & Call Transcripts:", 0, 100, 80)
        
        # Dynamic HTML Health Bar (Margin adjusted to 5px to prevent clipping)
        bar_color = "#2ECC71" if sentiment > 70 else "#F1C40F" if sentiment > 40 else "#E74C3C"
        st.markdown(f"""
            <div style="width: 100%; background-color: #1E2129; border-radius: 5px; margin-top: 5px; margin-bottom: 20px;">
                <div style="width: {sentiment}%; height: 12px; background-color: {bar_color}; border-radius: 5px; transition: width 0.3s, background-color 0.3s;"></div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**Recent Simulated Engagement Summary:**")
        if sentiment > 70:
            st.info(""" "Recent engagement data indicates a strong positive shift in account sentiment following the Q3 release. During a routine check-in call last Thursday, the primary platform admin explicitly noted that the new reporting dashboard is 'fantastic' and has directly eliminated their need for manual CSV exports—estimating a time savings of roughly 3 hours per week for their analytics team. This qualitative feedback is corroborated by product telemetry, which shows a 400% week-over-week increase in dashboard interaction by this account. Furthermore, a minor Zendesk ticket regarding a UI bug was resolved in under 2 hours, resulting in a 5/5 CSAT score and a follow-up email from their VP of Operations praising the support team's rapid responsiveness." """)
        elif sentiment > 40:
            st.warning(""" "Telemetry analysis over the past 14 days indicates an emerging adoption bottleneck within this account's middle-management tier, specifically regarding the Q3 reporting update. A recent Zendesk ticket explicitly stated, 'I am having some trouble finding the export button. Can you point me to the docs?' This qualitative friction is supported by backend product usage data, which shows the user abandoned the export workflow three times prior to submitting the ticket. Additionally, Staircase.AI sentiment analysis on recent email threads indicates a mild increase in frustration markers compared to last quarter, and recent Gong call snippets highlight confusion around the new UI layout. While overall license utilization remains stable, this localized friction presents an early-warning adoption risk. Recommending immediate deployment of contextual micro-training to the affected user cohort to accelerate time-to-value and prevent sentiment degradation." """)
        else:
            st.error(""" "Urgent churn risk detected. Telemetry and unstructured communication data indicate a severe degradation in account health over the past 30 days, primarily driven by infrastructure reliability. A Priority 1 support ticket was opened yesterday by their CTO explicitly stating, 'This is the third time the API has timed out this month. We are evaluating other vendors.' This qualitative escalation correlates directly with our backend telemetry, which confirms three distinct periods of elevated API latency exceeding contracted SLA thresholds. Furthermore, Staircase.AI sentiment tracking on the resulting email thread triggered a 'Flight Risk' alert, and a Gong transcript from last week's technical sync captured their Engineering Lead requesting a full export of historical data—a highly predictive leading indicator of competitor migration. With high-value ARR at stake and the renewal window rapidly closing, standard engagement playbooks must be bypassed. Recommending immediate executive alignment and an emergency technical post-mortem with our Product Engineering team to salvage the relationship." """)
            
    with col2:
        st.subheader("Dynamic Health Output")
        if sentiment > 70:
            st.metric(label="Account Status", value="Healthy", delta="Low Churn Risk")
            st.success("CSM Action: Monitor normally. Automated email to Advocacy team with a CSQA to add to advocacy pipeline.")
        elif sentiment > 40:
            st.metric(label="Account Status", value="At Risk - Friction Detected", delta="-15 Sentiment Drop", delta_color="inverse")
            st.warning("CSM Action: Automated email sent with targeted enablement collateral regarding export features. Follow up at next meeting")
        else:
            st.metric(label="Account Status", value="Critical - Executive Escalation", delta="-45 Sentiment Drop", delta_color="inverse")
            st.error("CSM Action: Churn Risk Playbook triggered. Immediate executive alignment call scheduled. Renewal flagged in forecast.")

# --- PLAYBOOK 2: AUTOMATED QBR GENERATOR ---
elif playbook == "2. Automated QBR Generator":
    import pandas as pd
    import numpy as np
    
    st.title("Zero-Touch Automated QBRs")
    st.markdown("Scaling value realization to the long-tail SMB segment.")
    st.divider()
    
    st.markdown("### Select Account to Generate:")
    account = st.selectbox("Account Tier:", ["Mid-Market (Acme Corp)", "SMB (TechNova)", "Startup (BetaFlow)"])
    
    if st.button("Simulate AI QBR Generation"):
        with st.spinner('Ingesting 90-day telemetry, cross-referencing Salesforce KPIs, generating value charts...'):
            time.sleep(2)
            
        st.success("✅ QBR Successfully Generated and Queued for CSM Approval.")
        
        # --- SLIDE 1: GENERATIVE SUMMARY ---
        st.markdown("### Slide 1: Auto-Generated Executive Summary")
        st.markdown(f"""
        <div class="metric-card">
        <h4>{account} - Q3 Value Realization</h4>
        <ul>
            <li><b>Goal Achievement:</b> Processed 14,500 transactions (112% of baseline goal).</li>
            <li><b>Time Saved:</b> AI workflows saved the client an estimated 45 operational hours.</li>
            <li><b>Adoption Metric:</b> 85% of active users have logged in the past 7 days.</li>
            <li><b>Recommended Next Step:</b> Upgrade API limits to accommodate Q4 seasonal volume spikes.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # --- SLIDE 2: HISTORICAL TREND ---
        st.markdown("### Slide 2: Adoption vs. ROI (90-Day Historical Trend)")
        
        weeks = [f"Wk {i}" for i in range(1, 13)]
        
        if "Acme" in account:
            adoption = np.linspace(200, 850, 12) + np.random.uniform(-30, 30, 12)
            roi = adoption * 0.4 
        elif "TechNova" in account:
            adoption = np.concatenate((np.linspace(50, 150, 8), np.linspace(250, 400, 4))) + np.random.uniform(-15, 15, 12)
            roi = adoption * 0.35
        else:
            adoption = np.linspace(10, 150, 12) + np.random.uniform(-25, 25, 12)
            roi = adoption * 0.5
            
        adoption = np.maximum(adoption, 0)
        roi = np.maximum(roi, 0)
            
        historical_chart_data = pd.DataFrame({
            'Automated Workflows Triggered (Adoption)': adoption,
            'Operational Hours Saved (ROI)': roi
        }, index=weeks)
        
        st.area_chart(historical_chart_data)
        st.caption("AI Note for CSM: Notice the correlation between the workflow adoption spikes and compounding hours saved. Use this historical visual to anchor the expansion proposal.")
        
        st.markdown("<br>", unsafe_allow_html=True)

        # --- SLIDE 3: INTERACTIVE SIMULATOR ---
        st.markdown("### Slide 3: Interactive Value Realization Simulator")
        st.markdown("Stop presenting static charts. Hand the customer the mouse and let them project their own ROI.")
        
        # Inherit the final adoption number from the historical chart to use as the baseline
        current_adoption = int(adoption[-1])
        
        target_adoption = st.slider("Target Q4 Feature Adoption (Weekly Workflow Triggers):", min_value=100, max_value=2500, value=max(current_adoption + 200, 850), step=50)
        
        current_roi = current_adoption * 0.4
        projected_roi = target_adoption * 0.4
        
        m1, m2, m3 = st.columns(3)
        m1.metric("Current State", f"{current_adoption} triggers", "Baseline")
        m2.metric("Target State", f"{target_adoption} triggers", f"{target_adoption - current_adoption} increase")
        
        roi_delta = int(projected_roi - current_roi)
        m3.metric("Projected Q4 Hours Saved", f"{int(projected_roi)} hrs", f"+{roi_delta} hrs reclaimed", delta_color="normal")
        
        historical_baseline_line = np.linspace(current_adoption/2, current_adoption, 12)
        projected_trajectory = np.linspace(current_adoption, target_adoption, 12)
        
        projection_chart_data = pd.DataFrame({
            'Historical Adoption Baseline': historical_baseline_line,
            'Customer-Projected Trajectory': projected_trajectory
        }, index=weeks)
        
        st.line_chart(projection_chart_data)
        st.caption(f"AI Note for CSM: The customer has established their own success criteria. Document the target of {target_adoption} triggers in Gainsight, and immediately send the Tier 3 expansion contract required to unlock that volume.")

# --- PLAYBOOK 3: CONTEXTUAL RELEASE NOTES ---
elif playbook == "3. Contextual Release Notes":
    st.title("Hyper-Personalized Release Notes")
    st.markdown("Driving feature adoption by reframing product updates into vertical-specific business outcomes and persona-driven value.")
    st.divider()
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 1. Select Engineering Update")
        feature = st.radio("Raw Changelog:", [
            "API Pipeline: Enabled multi-threaded querying. Latency reduced by 14ms.",
            "Reporting: Added CRON scheduling. Users can export dashboards to PDF via automated triggers."
        ])
        
        st.markdown("### 2. Define Audience Context")
        industry = st.selectbox("Industry Vertical:", ["Healthcare / Medical", "FinTech / Banking", "Retail / E-Commerce"])
        persona = st.selectbox("Target Persona:", ["Executive Sponsor (Focus: ROI & Strategy)", "Platform Admin (Focus: Ops & Setup)"])
        
    with col2:
        st.markdown("### 3. AI Segmented Output")
        
        # --- Generative Logic Matrix ---
        subject = ""
        context = ""
        value = ""
        
        if "API" in feature:
            subject = "Platform Update: Faster Backend Performance"
            if industry == "Healthcare / Medical":
                context = "speeds up access to critical patient records" if "Executive" in persona else "enables multi-threaded querying for your EHR integrations"
                value = "This means your clinical staff spends less time waiting on screens and more time on patient care, directly supporting your Q3 efficiency targets." if "Executive" in persona else "This drops latency by 14ms per call, completely eliminating the morning shift timeout errors your IT helpdesk has been fielding."
            elif industry == "FinTech / Banking":
                context = "accelerates transaction verification speeds" if "Executive" in persona else "optimizes our backend data pipeline for your secure financial workflows"
                value = "This ensures your high-frequency trading pipelines never bottleneck during market hours, protecting your revenue stream from latency slippage." if "Executive" in persona else "This multi-threaded architecture drops payload latency by 14ms, meaning your automated compliance checks will run significantly faster during end-of-day reconciliation."
            else: # Retail
                context = "processes inventory data significantly faster" if "Executive" in persona else "upgrades our API endpoints to handle multi-threaded queries"
                value = "This keeps your storefront perfectly synced with your warehouse during high-volume traffic spikes, preventing overselling and protecting your customer experience." if "Executive" in persona else "This 14ms latency reduction means your ERP syncing workflows won't throttle or time out during massive holiday inventory uploads."
                
        else: # Reporting feature
            subject = "New Feature: Automated Dashboard Delivery"
            if industry == "Healthcare / Medical":
                context = "automates the delivery of compliance and audit dashboards" if "Executive" in persona else "adds CRON scheduling to the reporting module"
                value = "You will now receive these critical regulatory overviews directly in your inbox every Monday, ensuring you have total visibility into HIPAA compliance without needing to log in." if "Executive" in persona else "You can now configure automated PDF exports for your department heads, saving you the hours you currently spend manually generating and emailing weekly utilization reports."
            elif industry == "FinTech / Banking":
                context = "automates the distribution of portfolio risk summaries" if "Executive" in persona else "enables CRON job scheduling for your audit dashboards"
                value = "This ensures your executive team receives automated PDF tear-sheets of total exposure before the market opens, streamlining your daily risk assessments." if "Executive" in persona else "This means you can completely automate the Friday compliance reporting run, freeing up your afternoon and ensuring auditors get standardized formats automatically."
            else: # Retail
                context = "automates the delivery of weekend sales performance metrics" if "Executive" in persona else "adds automated CRON scheduling to the analytics suite"
                value = "You'll now have a fully formatted PDF of your conversion rates and cart abandonment stats waiting in your inbox every Monday morning to drive your weekly strategy." if "Executive" in persona else "You can set up 'set-and-forget' PDF exports for your merchandising managers, eliminating those frantic Monday morning Slack requests for custom data pulls."

        # Compile the final output
        st.success(f"""
        **Subject:** {subject}
        
        Hi [Name],
        
        I wanted to share a quick update we just pushed to production that {context}. 
        
        **Why this matters for you:**
        {value}
        
        Let me know if you want to jump on a quick 10-minute call this week to review how to implement this for your team.
        
        Best,
        Sacha
        """)

# --- PLAYBOOK 4: EARLY WARNING ADOPTION ---
elif playbook == "4. Early Warning Adoption":
    st.title("Trigger-Based Micro-Training")
    st.markdown("Intercepting user friction at the exact moment of struggle to protect adoption and deflect Support tickets.")
    st.divider()
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Telemetry Simulator")
        st.markdown("Select a live user session to monitor, then simulate a friction event.")
        
        scenario = st.selectbox("Active User Session:", [
            "1. Platform Admin (Acme Corp) - Data Integration Setup",
            "2. Data Analyst (TechNova) - Custom Report Builder",
            "3. VP of Sales (BetaFlow) - Forecasting Module"
        ])
        
        trigger = st.button("Simulate UI Friction Event")
        
    with col2:
        st.subheader("System Response")
        
        if trigger:
            with st.spinner("Analyzing telemetry stream..."):
                time.sleep(1)
            
            if "Admin" in scenario:
                st.error("⚠️ Alert: 'Rage Clicking' detected. User failed API key validation 4 times in 90 seconds.")
                time.sleep(1)
                st.success("🤖 AI Action Taken: Automated email dispatched with targeted 45-second Loom tutorial on Auth Token formatting.")
                st.info("System Log: Gainsight NXT Timeline updated. Intervention successful. No human CSM action required.")
                
            elif "Analyst" in scenario:
                st.warning("⚠️ Alert: 'Idle Hover' detected. User spent 3+ minutes on 'Add Metric' screen without saving or executing.")
                time.sleep(1)
                st.success("🤖 AI Action Taken: Triggered contextual in-app modal highlighting the 'Calculated Fields' glossary and a 15-second GIF tutorial.")
                st.info("System Log: Support ticket successfully deflected. Feature adoption tracking metric incremented.")
                
            else: # VP Sales
                st.error("⚠️ Alert: 'Workflow Abandonment'. Executive user exited the forecasting module after 2 failed filter attempts.")
                time.sleep(1)
                st.success("🤖 AI Action Taken: High-value user friction detected. Micro-training suppressed. Drafted high-touch Slack message for CSM review.")
                
                st.markdown("""
                <div class="metric-card" style="margin-top: 10px;">
                <b>Drafted CSM Message (Pending Approval):</b><br>
                <i>"Hey Sarah, noticed you were trying to pull the Q3 forecast by territory. The new filtering logic can be tricky—I recorded a quick 30-sec custom walkthrough for you here: [Loom Link]. Let me know if you want me to just build and save the view for you!"</i>
                </div>
                """, unsafe_allow_html=True)
                
                st.info("System Log: Call-to-Action (CTA) generated in Gainsight. CSM alerted via internal Slack integration.")
                
        else:
            st.markdown("Monitoring continuous telemetry stream... System optimal.")

# --- PLAYBOOK 5: C360 ACCOUNT SUMMARY ---
elif playbook == "5. C360 Account Summary":
    st.title("AI C360 Account Synthesis")
    st.markdown("The 60-Second Prep: Distilling disparate CRM data into an immediate, action-oriented executive brief.")
    st.divider()
    
    col_sel, col_empty = st.columns([1, 1])
    with col_sel:
        account_scenario = st.selectbox("Select Account Profile to Synthesize:", [
            "1. Acme Corp (Mid-Market) - Capacity Constrained",
            "2. TechNova (Enterprise) - High Friction / Escalated",
            "3. BetaFlow (SMB) - The 'Silent' Risk"
        ])
    
    st.markdown("### Raw Unstructured Data Feed")
    
    # Dynamic Data based on selection
    if "Acme" in account_scenario:
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("License Utilization", "98%", "+5%", delta_color="normal")
        m2.metric("Open Support Tickets", "1", "-2", delta_color="inverse")
        m3.metric("NPS Score", "8", "+2", delta_color="normal")
        m4.metric("Days to Renewal", "45")
        
        crm_data = """
        * **Salesforce:** Key stakeholder update: Previous primary sponsor (VP Marketing) departed; David Chen assumed the role last week. No introductory call logged yet.
        * **Zendesk:** Escalated Ticket #8891 logged last month - "Current API rate limits are bottlenecking our end-of-month reporting pipelines."
        * **Jira:** Engineering fix deployed to production yesterday (PR #4492) expanding API throughput limits for this specific tenant cluster.
        * **Gong:** N/A (No calls in last 30 days).
        """
        
        alert_type = "📈 EXPANSION ALERT"
        synthesis = "Synthesized CRM and telemetry data indicate a highly engaged account currently restricted by capacity limits. Their primary friction point—a hard cap on API rate limits—caused notable frustration last month, but Jira integration confirms Engineering successfully deployed the expanded endpoint architecture yesterday (Ticket #4492), neutralizing the bottleneck. Contact enrichment flags a newly appointed Marketing Director assumed control last week. Historical churn risk mitigated; account is primed for upsell."
        next_steps = "1. Bypass standard automated check-in.\n2. Initiate personalized outreach to the new Marketing Director (David Chen) today.\n3. Deliver the successful API resolution as an immediate value-add.\n4. Pivot directly into a capacity planning discussion, positioning a Tier 3 license expansion before the renewal deadline."

    elif "TechNova" in account_scenario:
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("License Utilization", "62%", "-23%", delta_color="inverse")
        m2.metric("Open Support Tickets", "5", "+3", delta_color="inverse")
        m3.metric("NPS Score", "4", "-4", delta_color="inverse")
        m4.metric("Days to Renewal", "90")
        
        crm_data = """
        * **Salesforce:** Renewal pipeline marked as 'At Risk'. Competitor evaluation field flagged as True.
        * **Zendesk:** 3 Sev-2 tickets opened this week regarding SSO integration failures. Average first-reply time currently missing SLA by 4 hours.
        * **Jira:** SSO bug mapped to known issue (Epic-882). No ETA on sprint allocation.
        * **Gong:** Sentiment analysis on yesterday's admin sync flagged keywords: "budget cuts", "leadership is asking for ROI", and "too difficult to manage".
        """
        
        alert_type = "🚨 SEVERE CHURN RISK"
        synthesis = "Critical degradation across all health pillars. License utilization has plummeted 23% in the last month, directly correlating with 3 open Sev-2 tickets regarding SSO failures. Jira indicates no immediate engineering resolution is planned. Furthermore, Gong conversational intelligence caught the platform admin explicitly mentioning 'budget cuts' and 'ROI scrutiny' from leadership, validating the Salesforce flag for active competitor evaluation. The CSM is currently operating blindly regarding the technical delay."
        next_steps = "1. Trigger 'Executive Escalation' Playbook immediately.\n2. Schedule a technical alignment call with the client, the CSM, and a Solutions Architect to provide a workaround for the SSO bug.\n3. Pause all automated marketing and expansion nurtures.\n4. Generate an emergency Value Realization deck highlighting historical ROI to arm their admin against leadership budget cuts."

    else:
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("License Utilization", "12%", "-10%", delta_color="inverse")
        m2.metric("Open Support Tickets", "0", "0", delta_color="off")
        m3.metric("NPS Score", "N/A", "0", delta_color="off")
        m4.metric("Days to Renewal", "14")
        
        crm_data = """
        * **Salesforce:** SMB Tier. No human touchpoints logged in 180 days. Billing credit card is flagged as expiring in 10 days. 
        * **Zendesk:** Zero tickets submitted in the last 6 months.
        * **Telemetry:** Primary Admin account has not logged in for 45 days. End-user activity is isolated to a single feature (basic exports).
        * **Gong:** N/A.
        """
        
        alert_type = "⚠️ SILENT RISK (GHOSTING)"
        synthesis = "This is a classic 'watermelon' account—green on the surface due to a lack of support tickets, but red internally. Zero tickets over 6 months indicates abandonment, not satisfaction, validated by the primary admin failing to log in for 45 days. The account is purely relying on basic exports without adopting any sticky core features. With the renewal in 14 days and the billing mechanism expiring, this account will silently churn via payment failure if not intercepted."
        next_steps = "1. Trigger automated 'Payment Method Expiring' sequence immediately.\n2. Do NOT send standard renewal templates; deploy the 'Re-engagement / Executive Check-in' email sequence from the VP of CS.\n3. If no response in 48 hours, downgrade forecast probability to 10% and reallocate CSM resources to salvageable pipeline."

    st.info(crm_data)
    
    if st.button("Synthesize Executive Brief"):
        with st.spinner("LLM cross-referencing Salesforce, Zendesk, Jira, and Gong..."):
            time.sleep(1.5)
            
        st.markdown("### 🤖 Action-Oriented Brief")
        
        # Color coding the alert type dynamically
        if "EXPANSION" in alert_type:
            alert_color = "green"
        elif "SEVERE" in alert_type:
            alert_color = "red"
        else:
            alert_color = "orange"
            
        st.markdown(f"""
        <div style="background-color: #1E2129; padding: 20px; border-radius: 8px; border-left: 5px solid {alert_color};">
            <h4 style="color: {alert_color}; margin-top: 0px;">{alert_type}</h4>
            <p><b>Context & Synthesis:</b><br>{synthesis}</p>
            <p><b>Recommended Next Steps:</b><br>{next_steps.replace('\n', '<br>')}</p>
        </div>
        """, unsafe_allow_html=True)
