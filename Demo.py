import streamlit as st
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI-Driven CS Ops Architecture", layout="wide", initial_sidebar_state="expanded")

# --- CUSTOM CSS FOR 'DARK MODE / ENTERPRISE' VIBE ---
st.markdown("""
    <style>
    .main {background-color: #0E1117;}
    h1, h2, h3 {color: #FAFAFA;}
    .stButton>button {background-color: #2E86C1; color: white; border-radius: 5px; width: 100%;}
    .stButton>button:hover {background-color: #1B4F72;}
    .metric-card {background-color: #1E2129; padding: 20px; border-radius: 10px; border-left: 5px solid #2E86C1;}
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("CS Ops Playbooks")
st.sidebar.markdown("Select a module to simulate the AI architecture.")
playbook = st.sidebar.radio("Navigation", [
    "1. Predictive Health Score", 
    "2. Automated QBR Generator", 
    "3. Contextual Release Notes", 
    "4. Early Warning Adoption", 
    "5. C360 Account Summary"
])

# --- PLAYBOOK 1: PREDICTIVE HEALTH SCORE ---
if playbook == "1. Predictive Health Score":
    st.title("Predictive AI Health Score")
    st.markdown("Moving from reactive lagging indicators to proactive sentiment analysis.")
    st.divider()
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("LLM Sentiment Ingestion Engine")
        sentiment = st.slider("Simulate average tone across Support Tickets & Call Transcripts:", 0, 100, 80)
        
        st.markdown("**Recent Simulated Ticket Text:**")
        if sentiment > 70:
            st.info('"The new dashboard update is fantastic. It saved our team 3 hours this week."')
        elif sentiment > 40:
            st.warning('"I am having some trouble finding the export button. Can you point me to the docs?"')
        else:
            st.error('"This is the third time the API has timed out this month. We are evaluating other vendors."')
            
    with col2:
        st.subheader("Dynamic Health Output")
        if sentiment > 70:
            st.metric(label="Account Status", value="Healthy", delta="Low Churn Risk")
            st.success("CSM Action: Monitor normally. Add to advocacy pipeline.")
        elif sentiment > 40:
            st.metric(label="Account Status", value="At Risk - Friction Detected", delta="-15 Sentiment Drop", delta_color="inverse")
            st.warning("CSM Action: Send targeted enablement collateral regarding export features.")
        else:
            st.metric(label="Account Status", value="Critical - Executive Escalation", delta="-45 Sentiment Drop", delta_color="inverse")
            st.error("CSM Action: AI Playbook triggered. Immediate executive alignment call scheduled. Renewal flagged.")

# --- PLAYBOOK 2: AUTOMATED QBR GENERATOR ---
elif playbook == "2. Automated QBR Generator":
    st.title("Zero-Touch Automated QBRs")
    st.markdown("Scaling value realization to the long-tail SMB segment.")
    st.divider()
    
    st.markdown("### Select Account to Generate:")
    account = st.selectbox("Account Tier:", ["Mid-Market (Acme Corp)", "SMB (TechNova)", "Startup (BetaFlow)"])
    
    if st.button("Simulate AI QBR Generation"):
        with st.spinner('Ingesting 90-day telemetry, cross-referencing Salesforce KPIs, formatting PDF...'):
            time.sleep(2)
            
        st.success("✅ QBR Successfully Generated and Queued for CSM Approval.")
        
        st.markdown("### Auto-Generated Executive Summary")
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

# --- PLAYBOOK 3: CONTEXTUAL RELEASE NOTES ---
elif playbook == "3. Contextual Release Notes":
    st.title("Hyper-Personalized Release Notes")
    st.markdown("Driving feature adoption by reframing product updates into vertical-specific business outcomes.")
    st.divider()
    
    st.markdown("**Original Engineering Changelog:**")
    st.code("Updated data pipeline API endpoints. Enabled multi-threaded querying. Reduced latency by 14ms.")
    
    st.markdown("### Select Customer Vertical for AI Translation:")
    industry = st.selectbox("Industry:", ["Healthcare / Medical", "FinTech / Banking", "Retail / E-Commerce"])
    
    if industry == "Healthcare / Medical":
        result = "Faster access to patient records. Our new update reduces data retrieval times, ensuring your clinical staff can pull critical charts instantly without system lag, fully maintaining HIPAA compliance."
    elif industry == "FinTech / Banking":
        result = "Execute trades and verify transactions faster. We've upgraded the backend pipeline to handle multi-threaded queries, reducing latency so your secure financial workflows never bottleneck during market hours."
    else:
        result = "Keep up with the holiday rush. The platform now processes inventory data significantly faster, meaning your e-commerce storefront stays perfectly synced with your warehouse during high-volume traffic spikes."
        
    st.markdown("**AI Segmented Customer Email:**")
    st.info(result)

# --- PLAYBOOK 4: EARLY WARNING ADOPTION ---
elif playbook == "4. Early Warning Adoption":
    st.title("Trigger-Based Micro-Training")
    st.markdown("Intercepting user friction at the exact moment of struggle.")
    st.divider()
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Telemetry Simulator")
        st.markdown("Click below to simulate a user repeatedly failing a workflow in the UI.")
        trigger = st.button("Simulate User Friction (Repeated Clicks/Errors)")
        
    with col2:
        st.subheader("System Response")
        if trigger:
            st.error("⚠️ Alert: User 'jsmith@acme.com' detected abandoning 'Report Export' module.")
            time.sleep(1)
            st.success("🤖 AI Action Taken: Targeted 30-second Loom tutorial sent to jsmith@acme.com.")
            st.info("CSM Dashboard Updated: 'Intervention logged. No human action required.'")
        else:
            st.markdown("Monitoring telemetry stream... System optimal.")

# --- PLAYBOOK 5: C360 ACCOUNT SUMMARY ---
elif playbook == "5. C360 Account Summary":
    st.title("AI C360 Account Synthesis")
    st.markdown("The 60-Second Prep: Distilling disparate CRM data into immediate context.")
    st.divider()
    
    st.markdown("### Raw Unstructured Data (Salesforce + Zendesk + Jira)")
    col1, col2, col3 = st.columns(3)
    col1.metric("Open Support Tickets", "3", "-1")
    col2.metric("License Utilization", "98%", "Critical")
    col3.metric("NPS Score", "8", "+2")
    
    st.code("Notes: Client frustrated last month by API limit cap. Engineering pushed fix ticket #4492 yesterday. Renewal date is 45 days away. Marketing director changed last week.")
    
    if st.button("Synthesize Executive Brief"):
        with st.spinner("Synthesizing..."):
            time.sleep(1.5)
        st.markdown("### 🤖 Generative Brief for CSM")
        st.success("""
        **Account Status: Ready for Expansion.** The client is currently maxing out their license tier (98% utilization) and is approaching renewal in 45 days. The major technical blocker (API limit cap) that caused frustration last month was resolved by Engineering yesterday (Ticket #4492). 
        
        **Recommended Action:** Reach out to the newly appointed Marketing Director today. Frame the conversation around the successful API fix, and immediately pivot to an expansion proposal for the next licensing tier before the renewal window closes.
        """)
