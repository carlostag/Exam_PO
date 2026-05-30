import streamlit as st
import time
import pandas as pd
from questions import RAW_QUESTION_BANK

# 1. SESSION STATE INITIALIZATION
if "exam_started" not in st.session_state:
    st.session_state.exam_started = False
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "active_questions" not in st.session_state:
    st.session_state.active_questions = []
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}
if "exam_submitted" not in st.session_state:
    st.session_state.exam_submitted = False

# 2. APP HEADER
st.set_page_config(page_title="Production Optimisation Simulator", layout="centered")
st.title("🏭 Production Optimisation Exam Simulator")
st.subheader("MUCEIM - Master's Degree in Computational Engineering & Industrial Mathematics")

# 3. CONFIGURATION SCREEN
if not st.session_state.exam_started:
    st.markdown(
        f"""
        ### **Official Exam Specification Blueprint:**
        * **Total Database Size:** {len(RAW_QUESTION_BANK)} calibrated questions.
        * **Strict Distribution Structure:**
          * *Units 1, 2, 3, 4, 6, 7, 8, 9:* **11 questions each**
          * *Unit 5 (Job Shop Optimization):* **12 questions**
          * *Total Exam Length:* **100 Multiple-Choice Questions**
        * **Time Allowed:** 60 Minutes (Hard limit | 36 seconds average pace target)
        * **Grading System Protocol:** Correct: `+1` | Incorrect: `-0.5` | Unanswered: `0`
        * **Final Calibration:** Total points achieved divided by 10 (Highest reachable grade: `10.0`)
        """
    )
    st.divider()
    
    if st.button("🚀 Start 100-Question Blueprint Exam", type="primary", use_container_width=True):
        from questions import get_blueprint_exam
        # Generate the structured question matrix
        st.session_state.active_questions = get_blueprint_exam()
        
        # Pre-populate tracking maps cleanly
        st.session_state.user_answers = {i: None for i in range(len(st.session_state.active_questions))}
        st.session_state.start_time = time.time()
        st.session_state.exam_started = True
        st.session_state.exam_submitted = False
        st.rerun()

# 4. LIVE EXAM MODE
if st.session_state.exam_started and not st.session_state.exam_submitted:
    TOTAL_EXAM_SECONDS = 60 * 60  
    elapsed_time = time.time() - st.session_state.start_time
    remaining_seconds = max(0, TOTAL_EXAM_SECONDS - elapsed_time)
    
    if remaining_seconds <= 0:
        st.session_state.exam_submitted = True
        st.error("⏰ Time has expired! Your answers have been automatically submitted.")
        st.rerun()
        
    mins, secs = divmod(int(remaining_seconds), 60)
    timer_col, progress_col = st.columns([1, 3])
    with timer_col:
        st.metric(label="Time Remaining", value=f"{mins:02d}:{secs:02d}")
    with progress_col:
        answered_count = sum(1 for v in st.session_state.user_answers.values() if v is not None)
        total_q = len(st.session_state.active_questions)
        st.progress(answered_count / total_q, text=f"Progress: {answered_count}/{total_q} Questions Answered")
        
    st.divider()

    with st.form("exam_form"):
        for idx, q in enumerate(st.session_state.active_questions):
            st.markdown(f"#### **Q{idx+1}. {q['question']}**")
            st.caption(f"📍 Source Block: *{q['unit']}*")
            
            saved_answer = st.session_state.user_answers.get(idx)
            current_selection = st.radio(
                f"Select option for Q{idx+1}:",
                options=q["options"],
                index=None if saved_answer is None else q["options"].index(saved_answer),
                key=f"q_radio_{idx}",
                label_visibility="collapsed"
            )
            st.session_state.user_answers[idx] = current_selection
            st.write("") 
            
        st.divider()
        submit_btn = st.form_submit_button("Submit Exam Answers", type="primary", use_container_width=True)
        if submit_btn:
            st.session_state.exam_submitted = True
            st.rerun()

# 5. RESULTS SCREEN
if st.session_state.exam_submitted:
    st.header("📊 Performance Dashboard")
    
    correct_count = 0
    incorrect_count = 0
    unanswered_count = 0
    detailed_log = []
    total_q = len(st.session_state.active_questions)
    
    for idx, q in enumerate(st.session_state.active_questions):
        user_choice = st.session_state.user_answers.get(idx)
        correct_option_text = q["options"][q["correct"]]
        
        if user_choice is None:
            unanswered_count += 1
            status = "Unanswered"
            score_impact = 0.0
        elif user_choice == correct_option_text:
            correct_count += 1
            status = "Correct"
            score_impact = 1.0
        else:
            incorrect_count += 1
            status = "Incorrect"
            score_impact = -0.5
            
        detailed_log.append({
            "Question": f"Q{idx+1}",
            "Unit Category": q["unit"],
            "Your Selection": user_choice if user_choice else "Skipped",
            "Correct Answer": correct_option_text,
            "Status": status,
            "Points Gained": score_impact
        })
        
    raw_score = (correct_count * 1) + (incorrect_count * -0.5)
    scaled_grade = max(0.0, raw_score / 10) # Points divided by 10
    
    score_col1, score_col2, score_col3 = st.columns(3)
    score_col1.metric("Final Calibrated Mark (/10.0)", f"{round(scaled_grade, 2)}/10.0")
    score_col2.metric("Raw Net Points Balance", f"{raw_score} pts")
    score_col3.metric("True Selection Precision", f"{round((correct_count/total_q)*100, 1)}%")
    
    st.subheader("Distribution Summary")
    col_c, col_i, col_u = st.columns(3)
    col_c.success(f"🟢 Correct Answers: {correct_count}")
    col_i.error(f"🔴 Incorrect Errors: {incorrect_count}")
    col_u.info(f"⚪ Skipped/Unanswered: {unanswered_count}")
    
    st.subheader("📋 Detailed Review Matrix")
    df_review = pd.DataFrame(detailed_log)
    
    def highlight_status(val):
        if val == "Correct": return "background-color: #d4edda; color: #155724;"
        elif val == "Incorrect": return "background-color: #f8d7da; color: #721c24;"
        return "background-color: #e2e3e5; color: #383d41;"
        
    st.dataframe(df_review.style.map(highlight_status, subset=["Status"]), use_container_width=True, hide_index=True)
    
    if st.button("🔄 Reset Evaluation Simulator", use_container_width=True):
        st.session_state.exam_started = False
        st.session_state.exam_submitted = False
        st.session_state.active_questions = []
        st.session_state.user_answers = {}
        st.rerun()
