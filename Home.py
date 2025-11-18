from password_gate import require_password
require_password()
import streamlit as st

def recruitment_hub_page():
    # --- Page Configuration ---
    st.set_page_config(
        page_title="GPG Recruitment Hub Concept",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- Title and Introduction ---
    st.title("🏛️ Government People Group (GPG) Recruitment Hub")
    st.markdown("""
        The GPG Recruitment Hub is envisioned as a **unified, one-stop digital portal** designed to streamline and enhance all GPG-owned recruitment services.
        It aims to consolidate tools, data, and access points for users across the government ecosystem, supporting efficiency and data-driven decisions.
    """)
    st.subheader("Key Vision: A Single Source for GPG Recruitment Excellence")
    st.markdown("---")

    # --- Core Capabilities Section ---
    st.header("✨ Core Capabilities of the Recruitment Hub")

    # Capability 1: One-Stop Shop
    st.subheader("1. Unified Service Access")
    st.markdown("""
        The hub will act as a **one-stop shop** for accessing all **GPG-owned recruitment services**. 
        This simplifies the user journey by providing a single, intuitive place to start, replacing disparate links and systems.
    """)

    # Capability 2: Data Insight (GRID Interface)
    st.subheader("2. People Data & Insights (GRID Interface)")
    st.markdown("""
        Enables users to interact with **people-related data insight tools** by interfacing directly with the **GRID (Government Research & Insights Database)**. 
        This capability supports data-driven decision-making in recruitment strategy and talent mapping.
    """)
    
    # Capability 3: Job Advert Optimiser
    st.subheader("3. Job Advert Optimiser Capability")
    st.markdown("""
        Provides direct access to the **GPG Job Advert Optimiser capability**. 
        This tool helps hiring managers and HR teams create clearer, more inclusive, and higher-performing job advertisements.
    """)

    # Capability 4: Job Posting Portal
    st.subheader("4. Central Job Posting Portal (Potential)")
    st.markdown("""
        The hub **could become the portal for posting jobs**, particularly if technical or practical challenges prevent all jobs from being posted solely through the Shared Services for Government cluster ERPs (Enterprise Resource Planning systems).
    """)

    # Capability 5: ERP Integration Documentation
    st.subheader("5. ERP Engineer Integration Documents")
    st.markdown("""
        For **ERP engineers and technical teams**, the hub will provide a dedicated area for accessing critical **integration documentation**. 
        This includes documents for processes like Employee Transfer, CEI (Common External Interface), and CS Jobs developer documentation.
    """)

    # Capability 6: Online Testing Interface
    st.subheader("6. Online Test and Assessment Interface")
    st.markdown("""
        It could provide a straightforward **interface for setting up Online Test and Assessment test sessions**, standardising and centralising the initial candidate screening process.
    """)

    st.markdown("---")
    
    # --- Implementation & Access Sections ---

    st.header("⚙️ Implementation & Governance")

    # Capability 7: Iterative Development
    st.subheader("7. Iterative and Incremental Development")
    st.success("""
        The hub will be developed **iteratively and incrementally** based on evolving business priorities and user feedback. 
        This ensures rapid delivery of high-value features and allows the system to adapt efficiently.
    """)

    # Capability 8: Role-Based Access Management (RBAC)
    st.subheader("8. Role-Based Access Management (RBAC)")
    st.warning("""
        A **Role-Based Access Management capability** could be overlayed, ensuring users only see and interact with options appropriate to their role (e.g., a Hiring Manager sees different features than an ERP Engineer).
    """)
    

# Run the page function
if __name__ == "__main__":
    recruitment_hub_page()