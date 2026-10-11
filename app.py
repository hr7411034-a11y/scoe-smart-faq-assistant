
import re
import streamlit as st

# =====================================================
# 1. PAGE CONFIGURATION
# =====================================================
st.set_page_config(
    page_title="SCOE Smart FAQ Assistant",
    page_icon="🎓",
    layout="wide"
)

# =====================================================
# 2. PROFESSIONAL UI
# =====================================================
st.markdown("""
<style>
.stApp {
    background: #f4f7fc;
}
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}
.hero {
    background: linear-gradient(120deg, #172554, #3456a4);
    padding: 30px;
    border-radius: 18px;
    color: white;
    margin-bottom: 24px;
}
.hero h1 {
    color: white;
    font-size: 32px;
}
.hero p {
    color: #e0e7ff;
    font-size: 16px;
}
.info-card {
    background: white;
    border: 1px solid #e1e8f5;
    border-radius: 14px;
    padding: 18px;
    min-height: 110px;
}
.info-card h4 {
    color: #243b78;
    margin: 0 0 8px;
}
.info-card p {
    color: #64748b;
    font-size: 14px;
    margin: 0;
}
.section-title {
    color: #172554;
    font-size: 22px;
    font-weight: 700;
    margin-top: 24px;
    margin-bottom: 12px;
}
div[data-testid="stChatMessage"] {
    background: white;
    border: 1px solid #e3e9f5;
    border-radius: 14px;
    padding: 12px;
}
.stButton > button {
    border-radius: 10px;
    min-height: 44px;
    border: 1px solid #dbe3f4;
}
footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# 3. COLLEGE INFORMATION
# =====================================================
COLLEGE = {
    "name": "Saraswati College of Engineering",
    "short_name": "SCOE",
    "location": "Kharghar, Navi Mumbai, Maharashtra",
    "address": (
        "Plot No. 46, Sector 5, near MSEB Sub Station, "
        "Kharghar, Navi Mumbai - 410210"
    ),
    "website": "https://engineering.saraswatikharghar.edu.in/",
    "contact_page": (
        "https://engineering.saraswatikharghar.edu.in/contact-us/"
    ),
    "admission_phone": "9320299474 / 9320299475",
    "registrar_email": "registrarsaraswati@gmail.com",
    "exam_email": "examcell.scoe@gmail.com",
    "admission_email": "admissions.scoe@sce.edu.in",
    "accounts_phone": "9833782506"
}

# =====================================================
# 4. FAQ KNOWLEDGE BASE
# Add new questions by adding another dictionary here.
# =====================================================
FAQS = [
    {
        "category": "College Overview",
        "question": "Tell me about Saraswati College of Engineering",
        "keywords": [
            "about college", "about scoe", "college information",
            "college introduction", "history", "established",
            "college overview", "saraswati", "scoe"
        ],
        "answer": f"""
### 🎓 About Saraswati College of Engineering

**Saraswati College of Engineering (SCOE)** is an engineering
institution located in Kharghar, Navi Mumbai, Maharashtra.

- **Location:** {COLLEGE['location']}
- **Address:** {COLLEGE['address']}
- **Established:** 2004, according to the college website.
- **Official website:** {COLLEGE['website']}

The institution provides engineering education across several
technical disciplines. Its website describes a focus on engineering
education, research, and preparing students for industry requirements.

For the latest institutional information, refer to the official website.
"""
    },
    {
        "category": "Courses",
        "question": "Which courses and branches are available?",
        "keywords": [
            "course", "courses", "branch", "branches", "department",
            "departments", "program", "programs", "engineering branch",
            "computer engineering", "artificial intelligence",
            "machine learning", "data science", "mechanical",
            "civil", "automobile", "information technology"
        ],
        "answer": f"""
### 📚 Courses and Engineering Branches

The college website lists the following engineering programmes:

1. Computer Engineering
2. Computer Science and Engineering (Artificial Intelligence and Machine Learning)
3. Computer Science and Engineering (Data Science)
4. Information Technology
5. Mechanical Engineering
6. Civil Engineering
7. Automobile Engineering
8. M.E. Civil Engineering (Structural Engineering)

Programme availability, intake, and admission eligibility can change.
Check the current course list and admission brochure on the
[official college website]({COLLEGE['website']}).
"""
    },
    {
        "category": "Admissions",
        "question": "How can I apply for admission?",
        "keywords": [
            "admission", "apply", "application", "enroll",
            "eligibility", "documents required", "admission process",
            "entrance", "cap round", "counselling", "cutoff"
        ],
        "answer": f"""
### 🎓 Admission Process

Students should follow the admission procedure applicable to their
chosen programme and admission category.

1. Check the course eligibility criteria.
2. Review the relevant entrance-examination or merit requirements.
3. Complete the applicable application or counselling process.
4. Keep the required academic and identity documents ready.
5. Follow the official selection and document-verification instructions.
6. Confirm the prescribed fees and complete admission formalities.

**Admission enquiries:** {COLLEGE['admission_phone']}

**Email:** {COLLEGE['admission_email']}

Visit the [official college contact page]({COLLEGE['contact_page']})
for current admission guidance. Deadlines and procedures must be
confirmed from current official notices.
"""
    },
    {
        "category": "Contact",
        "question": "What is the college address?",
        "keywords": [
            "address", "location", "where is college", "directions",
            "reach college", "map", "located", "kharghar",
            "navi mumbai", "postal address"
        ],
        "answer": f"""
### 📍 College Address

**{COLLEGE['name']}**

{COLLEGE['address']}

**Admission contact:** {COLLEGE['admission_phone']}

**Official website:** {COLLEGE['website']}

You can use the address above in a maps application to plan your route.
Check the official contact page for the latest contact details.
"""
    },
    {
        "category": "Contact",
        "question": "How can I contact the college?",
        "keywords": [
            "contact", "phone", "telephone", "mobile number",
            "email", "mail id", "helpline", "registrar",
            "office number", "college number"
        ],
        "answer": f"""
### ☎️ College Contact Information

**Address:** {COLLEGE['address']}

**Admission contacts:** {COLLEGE['admission_phone']}

**Registrar email:** {COLLEGE['registrar_email']}

**Examination cell email:** {COLLEGE['exam_email']}

**Admission email:** {COLLEGE['admission_email']}

**Accounts section:** {COLLEGE['accounts_phone']}

For the latest details and department-specific enquiries, visit the
[official contact page]({COLLEGE['contact_page']}).
"""
    },
    {
        "category": "Fees",
        "question": "What are the college fees?",
        "keywords": [
            "fee", "fees", "fee structure", "tuition", "payment",
            "cost", "amount", "installment", "instalment",
            "scholarship", "concession", "refund"
        ],
        "answer": f"""
### 💳 Fees and Scholarships

The exact fee amount depends on the programme, academic year,
admission category, and applicable rules.

To confirm your fees:

1. Contact the college accounts section.
2. Ask for the latest fee structure for your programme.
3. Confirm payment deadlines and accepted payment methods.
4. Ask whether scholarships, concessions, or instalments apply.
5. Keep your payment receipts for reference.

**Accounts contact:** {COLLEGE['accounts_phone']}

Please verify the amount directly with the college. This chatbot
does not store a verified current fee schedule.
"""
    },
    {
        "category": "Examinations",
        "question": "How do I get examination information?",
        "keywords": [
            "exam", "examination", "exam cell", "timetable",
            "hall ticket", "schedule", "semester exam",
            "internal exam", "practical exam", "exam form"
        ],
        "answer": f"""
### 📝 Examination Information

Students should check official examination notices for timetables,
hall tickets, examination forms, practical examinations, and other
academic announcements.

1. Review the latest notice from the college or university.
2. Check your subject-wise examination schedule.
3. Confirm examination-form deadlines.
4. Keep your hall ticket and student identity card ready.
5. Contact the examination cell if you need clarification.

**Examination cell email:** {COLLEGE['exam_email']}

For confirmed dates, follow the latest official notification.
"""
    },
    {
        "category": "Results",
        "question": "How can I check my examination results?",
        "keywords": [
            "result", "results", "marks", "grades", "backlog",
            "kt", "revaluation", "seat number", "university result"
        ],
        "answer": f"""
### 📊 Examination Results

Students should use the official university or student portal
specified in the current examination notification.

1. Open the official result portal.
2. Select the relevant examination and semester.
3. Enter the requested student or examination details.
4. View and save the result.
5. Contact the examination department if there is an error.

For backlog examinations, revaluation, or missing results,
follow the current university procedure.

**Examination cell:** {COLLEGE['exam_email']}
"""
    },
    {
        "category": "Facilities",
        "question": "What facilities does the college provide?",
        "keywords": [
            "facility", "facilities", "library", "laboratory",
            "labs", "computer centre", "computer center",
            "sports", "canteen", "classroom", "workshop",
            "auditorium", "infrastructure"
        ],
        "answer": f"""
### 🏫 Campus Facilities

The college website describes facilities including:

- Classrooms and staff rooms
- Laboratories and workshops
- Library and computer centre
- Conference and examination halls
- Recreation and sports areas
- Canteen
- Training and placement cell

Availability, access rules, and timings may vary.
For updated details, consult the
[official college website]({COLLEGE['website']}).
"""
    },
    {
        "category": "Hostel",
        "question": "Does the college provide hostel facilities?",
        "keywords": [
            "hostel", "accommodation", "stay", "room",
            "residence", "hostel fee", "hostel availability",
            "hostel contact"
        ],
        "answer": f"""
### 🛏️ Hostel Information

The college website indicates that hostel assistance is available.
Confirm directly with the college whether accommodation is available
for your course and academic year.

Before applying, ask about:

1. Availability and eligibility.
2. Hostel fees and deposits.
3. Room arrangements and amenities.
4. Food arrangements and additional charges.
5. Application deadlines and hostel rules.

Check the [official college website]({COLLEGE['website']})
for current information. Do not assume that a room is guaranteed.
"""
    },
    {
        "category": "Placements",
        "question": "What is the placement process?",
        "keywords": [
            "placement", "placements", "job", "jobs", "recruiter",
            "recruiters", "company", "companies", "package",
            "salary", "placement cell", "internship", "interview",
            "training", "tpo"
        ],
        "answer": f"""
### 💼 Training and Placement Cell

The college's Placement Cell describes its role as helping students
prepare for industry requirements through training, workshops,
seminars, industrial training, and recruitment activities.

A typical placement process may involve:

1. Student registration and eligibility checks.
2. Resume preparation.
3. Aptitude and technical assessments.
4. Technical and HR interviews.
5. Selection updates and offer formalities.

Students can prepare by improving technical knowledge, aptitude,
communication, and project experience.

**Placement information:**
[Official Placement Cell page](https://engineering.saraswatikharghar.edu.in/placement-cell/)

Current recruiters, eligibility, and placement statistics should
be verified from the latest official placement information.
"""
    },
    {
        "category": "Academics",
        "question": "What are the college timings?",
        "keywords": [
            "timing", "timings", "opening time", "closing time",
            "college hours", "working hours", "lecture time",
            "office hours", "when college opens"
        ],
        "answer": f"""
### 🕒 College Timings

Lecture timings may vary by department, semester, practical sessions,
and the current timetable.

For accurate timings:

1. Check your department timetable.
2. Review official notices for timetable changes.
3. Contact the college office for administrative working hours.

**Official website:** {COLLEGE['website']}

The chatbot does not have a verified, current timetable.
"""
    },
    {
        "category": "Certificates",
        "question": "How can I get a bonafide certificate?",
        "keywords": [
            "bonafide", "certificate", "certificates",
            "student document", "documents", "student section",
            "leaving certificate", "transcript"
        ],
        "answer": f"""
### 📄 Student Certificates

For a bonafide certificate or another student document:

1. Contact the college office or student section.
2. Ask which application form is required.
3. Keep your student ID and enrolment details available.
4. Provide the purpose of the certificate if requested.
5. Confirm processing time and any applicable charges.

**College address:** {COLLEGE['address']}

Confirm the current procedure with the student section before applying.
"""
    },
    {
        "category": "AI and ML",
        "question": "Tell me about the Artificial Intelligence and Machine Learning branch",
        "keywords": [
            "aiml", "ai ml", "artificial intelligence",
            "machine learning", "ai branch", "ml branch",
            "data science", "python", "deep learning"
        ],
        "answer": """
### 🤖 Computer Science and Engineering (AI & ML)

The college lists Computer Science and Engineering
(Artificial Intelligence and Machine Learning) as one of its programmes.

AI and ML students commonly study topics such as:

- Programming and problem solving
- Data structures and algorithms
- Database management
- Probability and statistics
- Machine learning algorithms
- Deep learning and neural networks
- Data analysis and AI application development

The actual syllabus and semester-wise subjects depend on the
applicable curriculum. Consult the official department and syllabus
information for your academic scheme.
"""
    }
]


# =====================================================
# 5. SMARTER QUESTION MATCHING
# =====================================================
STOP_WORDS = {
    "a", "an", "the", "is", "are", "was", "were", "do", "does",
    "did", "i", "we", "you", "my", "me", "our", "your", "can",
    "could", "please", "tell", "about", "to", "of", "in", "on",
    "and", "or", "it", "there", "be", "get", "know", "want",
    "would", "should", "will", "have", "has", "had", "what",
    "when", "where", "which", "who", "how", "much", "many",
    "give", "explain", "information", "details", "detail",
    "college", "student", "students", "me", "for", "at",
    # Keep college-name tokens (SCOE/Saraswati) so overview questions remain matchable.
}

# Common ways users may phrase the same question
ALIASES = {
    "fees": ["fee", "fees", "tuition", "payment", "cost", "amount"],
    "fee": ["fee", "fees", "tuition", "payment", "cost", "amount"],
    "placement": ["placement", "placements", "recruitment", "jobs"],
    "jobs": ["placement", "placements", "recruitment", "jobs"],
    "hostel": ["hostel", "accommodation", "residence"],
    "exam": ["exam", "examination", "timetable", "hall ticket"],
    "exams": ["exam", "examination", "timetable", "hall ticket"],
    "result": ["result", "results", "marks", "grades"],
    "results": ["result", "results", "marks", "grades"],
    "address": ["address", "location", "directions"],
    "location": ["address", "location", "directions"],
    "contact": ["contact", "phone", "telephone", "email"],
    "phone": ["contact", "phone", "telephone", "number"],
    "email": ["contact", "phone", "telephone", "email"],
    "bonafide": ["bonafide", "certificate", "student document"],
    "aiml": ["aiml", "artificial intelligence", "machine learning"],
    "branch": ["branch", "course", "department", "programme"],
    "branches": ["branch", "course", "department", "programme"],
    "courses": ["branch", "course", "department", "programme"],
    "facilities": ["facility", "facilities", "library", "laboratory"],
    "facility": ["facility", "facilities", "library", "laboratory"],
    "timings": ["timing", "timings", "working hours"],
    "timing": ["timing", "timings", "working hours"]
}


def tokenize(text):
    words = re.findall(r"[a-z0-9]+", text.lower())
    expanded = set(words)

    for word in words:
        if word in ALIASES:
            for alias in ALIASES[word]:
                expanded.update(re.findall(r"[a-z0-9]+", alias))

    return expanded - STOP_WORDS


def get_answer(user_question):
    query = re.sub(r"\s+", " ", user_question.lower()).strip()

    if not query:
        return "Please type a question so I can help you."

    # Handle greetings before FAQ matching.
    if query in {"hi", "hello", "hey", "good morning",
                 "good afternoon", "good evening"}:
        return (
            "Hello! 👋 Welcome to the SCOE Smart FAQ Assistant.\n\n"
            "I can help you explore college information, courses, admissions, "
            "fees, examinations, facilities, placements, and more."
        )

    # Route clear intents before fuzzy keyword scoring. Specific topics come first
    # so "AI and ML branch" cannot be mistaken for the general courses FAQ.
    intent_rules = [
        (
            "AI and ML",
            r"\b(ai\s*(?:and|&|n)?\s*ml|aiml|artificial intelligence|machine learning|deep learning)\b",
        ),
        (
            "Courses",
            r"\b(course|courses|branch|branches|department|departments|programme|programmes|program|programs|data science|computer engineering|information technology|mechanical engineering|civil engineering|automobile engineering)\b",
        ),
        (
            "Fees",
            r"\b(fee|fees|tuition|pay|payment|payments|cost|amount|installment|instalment|scholarship|concession|refund|charges?)\b",
        ),
        (
            "Placements",
            r"\b(placement|placements|placement cell|recruitment|recruiter|recruiters|job|jobs|salary|package|internship|tpo)\b",
        ),
        (
            "Facilities",
            r"\b(facility|facilities|library|laborator(?:y|ies)|labs?|canteen|sports|workshop|infrastructure|auditorium|computer centre|computer center)\b",
        ),
        (
            "Admissions",
            r"\b(admission|admissions|apply|application|enrol|enroll|eligibility|cutoff|cut-off|cap round|counselling|counseling)\b",
        ),
        (
            "Examinations",
            r"\b(exam|exams|examination|timetable|hall ticket|semester exam|exam form)\b",
        ),
        (
            "Results",
            r"\b(result|results|marks|grades|backlog|kt|revaluation|seat number)\b",
        ),
        (
            "Hostel",
            r"\b(hostel|accommodation|residence|hostel fee)\b",
        ),
        (
            "Certificates",
            r"\b(bonafide|certificate|certificates|leaving certificate|transcript)\b",
        ),
        (
            "Contact",
            r"\b(contact|phone|telephone|mobile number|email|mail id|helpline|registrar|office number|accounts number)\b",
        ),
        (
            "Contact",
            r"\b(address|location|directions|where is the college|where is scoe|reach college|kharghar|navi mumbai)\b",
        ),
        (
            "Academics",
            r"\b(timing|timings|opening time|closing time|college hours|working hours|lecture time|office hours)\b",
        ),
        (
            "College Overview",
            r"\b(about scoe|about saraswati|tell me about scoe|tell me about saraswati|college overview|college introduction|college information|history|established|what is scoe)\b",
        ),
    ]

    for category, pattern in intent_rules:
        if re.search(pattern, query):
            # For location questions, prefer the address FAQ over general contact details.
            if category == "Contact" and re.search(
                r"\b(address|location|directions|where is the college|where is scoe|reach college|kharghar|navi mumbai)\b",
                query,
            ):
                for faq in FAQS:
                    if faq["question"] == "What is the college address?":
                        return faq["answer"]

            for faq in FAQS:
                if faq["category"] == category:
                    # The FAQ list contains two Contact entries; select the
                    # dedicated contact FAQ unless the query asked for location.
                    if category == "Contact" and faq["question"] != "How can I contact the college?":
                        continue
                    return faq["answer"]

    query_words = tokenize(query)

    if not query_words:
        # College-name-only queries should still be understood as overview requests.
        if re.search(r"\b(scoe|saraswati)\b", query):
            return next(
                faq["answer"] for faq in FAQS
                if faq["category"] == "College Overview"
            )
        return (
            "Please ask a more specific question. For example, "
            "'What is the college address?' or 'How can I apply for admission?'"
        )

    best_faq = None
    best_score = 0
    second_best_score = 0

    for faq in FAQS:
        question_words = tokenize(faq["question"])
        keyword_words = tokenize(" ".join(faq["keywords"]))

        score = (
            2 * len(query_words.intersection(question_words))
            + len(query_words.intersection(keyword_words))
        )

        for keyword in faq["keywords"]:
            if len(keyword) > 3 and keyword in query:
                score += 2

        if faq["question"].lower() in query:
            score += 5

        if score > best_score:
            second_best_score = best_score
            best_score = score
            best_faq = faq
        elif score > second_best_score:
            second_best_score = score

    # Avoid weak or ambiguous matches rather than confidently returning an unrelated FAQ.
    if best_faq is not None and best_score >= 2:
        if second_best_score and best_score - second_best_score <= 1:
            return (
                "I found a couple of possible topics. Could you be more specific?\n\n"
                "Try asking about fees, admissions, courses, placements, "
                "facilities, examinations, results, hostel, or college contacts."
            )
        return best_faq["answer"]

    return (
        "I'm sorry, I couldn't confidently match that question to my "
        "college FAQ knowledge base.\n\n"
        "You can ask me about:\n"
        "- College overview and address\n"
        "- Courses and AI & ML branch\n"
        "- Admissions and fees\n"
        "- Examinations and results\n"
        "- Certificates and facilities\n"
        "- Hostel and placements\n"
        "- College contacts and timings\n\n"
        "For information not covered here, please consult the official "
        "college website or the relevant college department."
    )

# =====================================================
# 6. SIDEBAR
# =====================================================
with st.sidebar:
    st.markdown("# 🎓 SCOE Assistant")
    st.caption("Saraswati College of Engineering")
    st.divider()

    st.markdown("### Explore topics")

    for topic in [
        "🏫 About the College",
        "📚 Courses",
        "🎓 Admissions",
        "💳 Fees",
        "📝 Examinations",
        "📊 Results",
        "🏢 Facilities",
        "🛏️ Hostel",
        "💼 Placements",
        "🤖 AI & ML",
        "☎️ Contact"
    ]:
        st.write(topic)

    st.divider()

    st.markdown("### Official resources")
    st.markdown(f"[College Website]({COLLEGE['website']})")
    st.markdown(f"[Contact Page]({COLLEGE['contact_page']})")

    if st.button("🔄 Clear Chat", use_container_width=True):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Hello! 👋 Welcome to the SCOE Smart FAQ Assistant. "
                    "Ask me about college information, courses, admissions, "
                    "fees, examinations, placements, and facilities."
                )
            }
        ]
        st.rerun()


# =====================================================
# 7. MAIN DASHBOARD
# =====================================================
st.markdown("""
<div class="hero">
    <h1>🎓 SCOE Smart FAQ Assistant</h1>
    <p>
        Your digital guide to Saraswati College of Engineering.
        Ask questions and explore college information in seconds.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card">
        <h4>📚 College Knowledge</h4>
        <p>Information about departments, courses and facilities.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h4>⚡ Smart Matching</h4>
        <p>Keyword scoring and aliases for common questions.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <h4>💬 Student Support</h4>
        <p>Quick answers with official links and contact details.</p>
    </div>
    """, unsafe_allow_html=True)


# =====================================================
# 8. CHAT INTERFACE
# =====================================================
st.markdown(
    '<div class="section-title">💬 Ask the SCOE Assistant</div>',
    unsafe_allow_html=True
)

WELCOME = (
    "Hello! 👋 Welcome to the SCOE Smart FAQ Assistant.\n\n"
    "I can answer questions about Saraswati College of Engineering, "
    "including its courses, admissions, fees, examinations, facilities, "
    "placements, and contact information.\n\n"
    "What would you like to know?"
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": WELCOME}
    ]

# Display existing conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle typed questions
if prompt := st.chat_input("Ask about SCOE, courses, fees, placements..."):
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    response = get_answer(prompt)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.rerun()


# =====================================================
# 9. POPULAR QUESTIONS
# =====================================================
st.markdown(
    '<div class="section-title">✨ Popular Questions</div>',
    unsafe_allow_html=True
)

suggestions = [
    "Tell me about SCOE",
    "What courses are available?",
    "What is the college address?",
    "How do I apply for admission?",
    "What are the college fees?",
    "Tell me about placements",
    "What facilities are available?",
    "Tell me about the AI and ML branch"
]

left, right = st.columns(2)

for index, question in enumerate(suggestions):
    target = left if index % 2 == 0 else right

    with target:
        if st.button(
            question,
            key=f"popular_{index}",
            use_container_width=True
        ):
            st.session_state.messages.append(
                {"role": "user", "content": question}
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": get_answer(question)
                }
            )

            st.rerun()


# =====================================================
# 10. FOOTER
# =====================================================
st.divider()

st.caption(
    "SCOE Smart FAQ Assistant | Student Project Prototype | "
    "Verify time-sensitive details with official college sources."
)
