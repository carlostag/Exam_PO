import streamlit as st
import time
import pandas as pd
# Pull the raw question pool directly from your questions.py file
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
st.subheader("MUCEIM - Master's in Computational Engineering & Industrial Mathematics")

# 3. CONFIGURATION SCREEN (Before Exam Starts)
if not st.session_state.exam_started:
    st.markdown(
        f"""
        **Official Exam Specification Framework:**
        * **Total Available Database Question Pool:** {len(RAW_QUESTION_BANK)} items
        * **Standard Exam Length:** 100 questions (randomly pulled from pool)
        * **Time Limit:** 60 Minutes (36 seconds per question target pace)
        * **Grading Protocol:** Correct: `+1 point` | Incorrect: `-0.5 points` | Unanswered/Skipped: `0 points`
        * **Final Calibration:** Points achieved divided by 10 (Maximum reachable grade: `10.0`)
        """
    )
    st.divider()
    
    # Select desired number of questions
    max_available = len(RAW_QUESTION_BANK)
    default_selection = min(100, max_available)
    
    selected_num = st.slider(
        "🎛️ Select the number of simulation questions to pull:",
        min_value=5,
        max_value=max_available,
        value=default_selection,
        step=5
    )
    
    st.write(f"Your selected pace target: **{round((60 * 60) / selected_num, 1)} seconds** per question.")

    if st.button("🚀 Start Production Optimisation Exam", type="primary", use_container_width=True):
        from questions import get_randomized_exam
        st.session_state.active_questions = get_randomized_exam(selected_num)
        
        # Ensure user_answers dictionary is cleanly pre-populated
        st.session_state.user_answers = {i: None for i in range(len(st.session_state.active_questions))}
        st.session_state.start_time = time.time()
        st.session_state.exam_started = True
        st.session_state.exam_submitted = False
        st.rerun()

# 4. LIVE EXAM MODE
if st.session_state.exam_started and not st.session_state.exam_submitted:
    
    # Timer logic
    TOTAL_EXAM_SECONDS = 60 * 60  # 60 minutes
    elapsed_time = time.time() - st.session_state.start_time
    remaining_seconds = max(0, TOTAL_EXAM_SECONDS - elapsed_time)
    
    # Auto-submit trigger if time runs out
    if remaining_seconds <= 0:
        st.session_state.exam_submitted = True
        st.error("⏰ Time has expired! Your responses have been automatically submitted.")
        st.rerun()
        
    # Render visible timer metrics
    mins, secs = divmod(int(remaining_seconds), 60)
    timer_col, progress_col = st.columns([1, 3])
    with timer_col:
        st.metric(label="Time Remaining", value=f"{mins:02d}:{secs:02d}")
    with progress_col:
        answered_count = sum(1 for v in st.session_state.user_answers.values() if v is not None)
        total_q = len(st.session_state.active_questions)
        st.progress(answered_count / total_q, text=f"Progress: {answered_count}/{total_q} Questions Completed")
        
    st.divider()

    # Form containing quiz questions
    with st.form("exam_form"):
        for idx, q in enumerate(st.session_state.active_questions):
            st.markdown(f"#### **Q{idx+1}. [{q['unit']}] {q['question']}**")
            
            saved_answer = st.session_state.user_answers.get(idx)
            
            current_selection = st.radio(
                f"Select option for Q{idx+1}:",
                options=q["options"],
                index=None if saved_answer is None else q["options"].index(saved_answer),
                key=f"q_radio_{idx}",
                label_visibility="collapsed"
            )
            st.session_state.user_answers[idx] = current_selection
            st.write("") # Spacer
            
        st.divider()
        submit_btn = st.form_submit_button("Submit Exam Answers", type="primary", use_container_width=True)
        
        if submit_btn:
            st.session_state.exam_submitted = True
            st.rerun()

# 5. RESULTS & GRADING SCREEN
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
            "Unit Source": q["unit"],
            "Your Selection": user_choice if user_choice else "Skipped",
            "Correct Answer": correct_option_text,
            "Status": status,
            "Points Gained": score_impact
        })
        
    # Calculate Score Points
    raw_score = (correct_count * 1) + (incorrect_count * -0.5)
    
    # Official scale rule: points achieved divided by 10 (capped dynamically if pulling fewer than 100 items)
    if total_q == 100:
        scaled_grade = raw_score / 10
    else:
        # Balanced scaling adjustment for alternative testing sizes
        scaled_grade = (raw_score / total_q) * 10 if total_q > 0 else 0
        
    final_calibrated_grade = max(0.0, round(scaled_grade, 2))
    
    # Display Score Metrics
    score_col1, score_col2, score_col3 = st.columns(3)
    score_col1.metric("Final Scale Mark (/10.0)", f"{final_calibrated_grade}/10.0")
    score_col2.metric("Raw Evaluation Balance", f"{raw_score} pts")
    score_col3.metric("True Precision Rate", f"{round((correct_count/total_q)*100, 1) if total_q > 0 else 0}%")
    
    st.subheader("Distribution Balance Breakdown")
    col_c, col_i, col_u = st.columns(3)
    col_c.success(f"🟢 Correct Answers: {correct_count}")
    col_i.error(f"🔴 Incorrect Errors: {incorrect_count}")
    col_u.info(f"⚪ Skipped/Unanswered: {unanswered_count}")
    
    # Detail Review Table
    st.subheader("📋 Granular Solution Review")
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
