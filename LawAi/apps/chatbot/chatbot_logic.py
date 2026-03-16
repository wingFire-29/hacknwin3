"""
Chatbot logic for LawAi - Legal AI Assistant
Handles user queries and generates appropriate responses
"""

import re

# Knowledge base for legal queries
LEGAL_KNOWLEDGE_BASE = {
    'ipc': {
        'keywords': ['ipc', 'section', 'indian penal code'],
        'response': """The Indian Penal Code (IPC) is the main criminal law of India. Here are some common sections:

**Common IPC Sections:**
- **Section 302**: Punishment for murder
- **Section 304**: Culpable homicide not amounting to murder
- **Section 380**: Theft
- **Section 392**: Punishment for dacoity
- **Section 420**: Cheating
- **Section 498A**: Cruelty by husband/family

Each section has specific punishment and conditions. For detailed information, please consult with a qualified lawyer."""
    },
    'fraud': {
        'keywords': ['fraud', 'scam', 'deceived', 'cheat', 'online fraud', 'complaint'],
        'response': """**Steps to file a complaint for fraud:**

1. **Report to Cybercrime Portal**
   - Visit: www.cybercrime.gov.in (National Cyber Crime Portal)
   - File complaint online with details and evidence

2. **Local Police Station**
   - Visit nearest police station with documents
   - Provide transaction details, screenshots, and evidence
   - Get First Information Report (FIR) copy

3. **Evidence to gather:**
   - Screenshots of transactions
   - Email/message conversations
   - Banking statements
   - Identity of fraudster (if known)
   - Screenshots of website/app used

4. **RBI/Bank Complaint**
   - Contact your bank immediately
   - Report unauthorized transactions
   - Request dispute resolution

**Under IPC:**
- Section 420: Cheating
- Section 406: Criminal breach of trust
- Section 120B: Criminal conspiracy (if applicable)

Keep all evidence safe and maintain copies of FIR filed."""
    },
    'contract': {
        'keywords': ['contract', 'agreement', 'draft', 'terms', 'document'],
        'response': """**Essential elements of a valid contract:**

1. **Offer and Acceptance**
   - Clear offer by one party
   - Unconditional acceptance by other

2. **Consideration**
   - Something of value exchanged
   - Must be legally binding

3. **Intention to Create Legal Relations**
   - Parties must intend to be legally bound

4. **Capacity**
   - Parties must be of legal age
   - Must be of sound mind

5. **Legality**
   - Contract purpose must be legal
   - Cannot violate laws

**Tips for contract drafting:**
- Be specific and clear
- Define all terms explicitly
- Include dispute resolution clause
- Mention jurisdiction and governing law
- Get legal review before signing

**Common contract types:**
- Employment agreement
- Sales agreement
- Lease agreement
- Partnership agreement

Always consult a lawyer before signing important contracts."""
    },
    'divorce': {
        'keywords': ['divorce', 'separation', 'alimony', 'custody', 'matrimonial'],
        'response': """**Types of Divorce in India:**

1. **Mutual Divorce**
   - Both parties agree
   - Faster process (6 months - 2 years)
   - Less costly

2. **Contested Divorce**
   - One party opposes
   - Longer process (3-5 years)
   - Requires evidence

**Grounds for Divorce:**
- Adultery
- Cruelty
- Desertion
- Conversion to different religion
- Unsound mind
- Leprosy/venereal disease
- Separation (for mutual divorce)

**Important considerations:**
- Alimony/maintenance
- Child custody
- Property division
- Guardianship rights

**Procedure:**
- Petition filing in family court
- Service of notice
- Opportunity to respond
- Court proceedings
- Final decree

This is complex - professional legal advice is essential."""
    },
    'property': {
        'keywords': ['property', 'real estate', 'land', 'deed', 'ownership', 'title'],
        'response': """**Property Rights and Ownership:**

**Types of property:**
1. **Immovable Property**
   - Land, buildings, structures
   - Registered under Registration Act

2. **Movable Property**
   - Vehicles, goods, materials
   - Can be transferred easily

**Property Registration:**
- Mandatory for immovable property
- Protects ownership
- Transfer of property deed

**Documents needed:**
- Title deeds
- Sale agreement
- Property survey map
- Tax receipts
- NOC from authorities

**Common issues:**
- Boundary disputes with neighbors
- Invalid titles
- Encroachment
- Inheritance conflicts

**Steps to purchase property:**
1. Verify title and ownership
2. Check if property is dispute-free
3. Get property inspected
4. Negotiate price
5. Register the property
6. Get possession

Always get title verification and legal inspection before buying property."""
    },
    'rights': {
        'keywords': ['rights', 'fundamental rights', 'responsibilities', 'duties', 'constitution'],
        'response': """**Fundamental Rights in India (Constitution):**

**Article 14**: Equality before law
**Article 19**: Freedom of speech, expression, assembly
**Article 21**: Right to life and liberty
**Article 25-28**: Religious freedom
**Article 29-30**: Minority rights
**Article 32**: Right to constitutional remedies

**Duties of Citizens:**
- Respect Constitution
- Follow laws
- Defend nation
- Promote harmony
- Protect natural heritage
- Develop scientific outlook

**Types of writs available:**
- **Habeas Corpus**: Against unlawful detention
- **Mandamus**: Compel authority to perform duty
- **Prohibition**: Stop illegal action
- **Quo Warranto**: Challenge authority
- **Certiorari**: Review court decision

**Where to file:**
- High Court
- Supreme Court
- District Court (in some cases)

Your rights come with responsibilities. Know your rights and exercise them responsibly."""
    },
    'employment': {
        'keywords': ['employment', 'labor', 'wage', 'termination', 'workplace', 'boss', 'job'],
        'response': """**Employee Rights in India:**

**Wages and Working Hours:**
- Fair wages for work
- Overtime payment
- Leave (sick, casual, annual)
- Bonus (if eligible)

**Types of Leave:**
- Casual Leave: 5-10 days/year
- Sick Leave: 10-15 days/year
- Annual Leave: 15-20 days/year
- Maternity Leave: 26 weeks
- Paternity Leave: 15 days

**Protection from:**
- Unfair termination
- Sexual harassment
- Discrimination
- Unsafe working conditions
- Forced labor

**Termination:**
- Notice period typically 30 days
- Severance pay if not at fault
- Gratuity benefits
- Benefits of notice period salary

**File complaints to:**
- Labour Commissioner
- Industrial Tribunal
- District Court
- National Labour Commission

**Important laws:**
- Factories Act
- Industrial Disputes Act
- Minimum Wages Act
- Sexual Harassment Act

Know your rights - report violations immediately."""
    },
    'loan': {
        'keywords': ['loan', 'debt', 'interest', 'npa', 'default', 'bank', 'credit'],
        'response': """**Loan and Debt Laws in India:**

**Types of Loans:**
- Personal loans
- Home loans (mortgages)
- Auto loans
- Education loans
- Business loans

**Your Rights as Borrower:**
- Know exact interest rate
- Clear EMI schedule
- No hidden charges
- Right to foreclose early
- Protection against harassment

**Steps if you can't pay:**
1. Contact lender immediately
2. Negotiate new terms
3. Request restructuring
4. Debt consolidation option

**Protection from:**
- Abusive recovery practices
- Harassment beyond office hours
- Threats or violence
- Publishing private information
- Illegal attachment of property

**Legal remedies:**
- Consumer Protection Act
- Reserve Bank of India grievance
- Finance Ombudsman
- District Court lawsuit
- Insolvency proceedings

**What lenders CAN do:**
- Send reminders
- Legal notices
- Court action
- Asset attachment (through court)

**What lenders CANNOT do:**
- Harassment outside office hours
- Use abusive language
- Publish personal information
- Use physical threats
- Illegal property seizure

Always contact a lawyer if facing illegal recovery practices."""
    }
}


def get_chatbot_response(user_message):
    """
    Generate a chatbot response based on user message
    Uses keyword matching to identify the topic
    """
    user_message_lower = user_message.lower()
    
    # Check against knowledge base
    for topic, data in LEGAL_KNOWLEDGE_BASE.items():
        for keyword in data['keywords']:
            if keyword in user_message_lower:
                return data['response']
    
    # Default response for unknown queries
    return generate_default_response(user_message)


def generate_default_response(user_message):
    """Generate response for queries not in knowledge base"""
    
    # Check for greetings
    greetings = ['hello', 'hi', 'hey', 'how are you', 'good morning', 'good evening', 'good afternoon']
    if any(greeting in user_message.lower() for greeting in greetings):
        return """Good day! 👋 I'm LawAi, your legal assistant. I can help you with:

**Legal topics I can assist with:**
- IPC sections and criminal law
- Filing fraud complaints
- Contract drafting
- Divorce and family law
- Property and real estate
- Constitutional rights
- Employment law
- Loan and debt issues

How can I help you today?"""
    
    # Check for thank you
    if any(phrase in user_message.lower() for phrase in ['thank', 'thanks', 'thankyou']):
        return "You're welcome! If you have any other questions about Indian law, feel free to ask. 😊"
    
    # Default response
    return f"""I understand you're asking about: "{user_message}"

While I don't have specific information about this topic, I can help with:
- IPC sections and criminal law
- Fraud and cybercrime complaints
- Contracts and agreements
- Divorce and family matters
- Property laws
- Constitutional rights
- Employment law
- Loan and debt issues

**For your query, I recommend:**
1. Consult with a qualified lawyer
2. Visit your nearest legal aid center
3. Contact relevant government authority

Would you like information on any of the topics I mentioned?"""