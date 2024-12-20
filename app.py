import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
import os  # Add this import to work with environment variables

def run(text_input):
    genai.configure(api_key="AIzaSyD-Mu1--Ob42X5JA4w9thLZJtOd8YuWpYU")  # Use the passed API key

    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro-002",
        generation_config=generation_config,
    )

    chat_session = model.start_chat()

    textuser = text_input
    prompt = ('''Shivajirao Kadam Institute of Technology & Management (SKITM) is a prominent educational institution located in Indore, Madhya Pradesh, India. Established in 2019, SKITM offers a diverse range of undergraduate and postgraduate programs across various disciplines.

        Academic Programs:

        Engineering:

        B.Tech. in Computer Science Engineering
        B.Tech. in Computer Science Engineering - Artificial Intelligence & Machine Learning
        B.Tech. in Computer Science Engineering - Information Technology
        B.Tech. in Computer Science Engineering - Data Science
        B.Tech. in Information Technology
        B.Tech. in Electronics & Communication Engineering
        B.Tech. in Civil Engineering
        B.Tech. in Mechanical Engineering
        Management:

        Master of Business Administration (MBA)
        Integrated Master of Business Administration (UG+PG)
        Pharmaceutical Sciences:

        Bachelor of Pharmacy
        Diploma in Pharmacy
        Master of Pharmacy
        Law:

        B.A. LL.B. (Hons.)
        B.B.A. LL.B. (Hons.)
        LL.B. (Hons.)
        Professional Studies:

        Bachelor of Business Administration
        Bachelor of Commerce
        Bachelor of Commerce (Computer Application)
        Performing Arts:

        Diploma in Dance & Music
        Mission and Vision:

        SKITM is committed to developing a center of excellence in education, integrating scientific and modern technical knowledge with human values. The institution aims to provide students with quality education and practical training to tackle global technology challenges, competitiveness, and entrepreneurship. 
        SKITM

        Placements:

        The institute boasts a strong placement record, with top recruiting companies such as TCS, Wipro, Infosys, and others visiting the campus. The highest salary package offered is around 18 LPA, with an average salary package of about 4.5 LPA. In the Computer Science Engineering branch, the placement percentage is 100%. 
        SHIKSHA

        Campus and Facilities:

        SKITM offers state-of-the-art infrastructure, including well-equipped laboratories, modern classrooms, and a comprehensive library. The campus is designed to provide a conducive environment for learning and personal growth.

        Accreditation and Affiliation:

        SKITM is affiliated with the Transnational Knowledge Society and adheres to the guidelines set by the Directorate of Technical Education, Madhya Pradesh.







        The best college in Indore.
        SKITM is an academician-led Institute founded by Prof. Shivajirao Kadam, Chancellor of Bharati Vidyapeeth Pune, India’s leading University. The group has colleges in the areas of Engineering, Law, Management, Pharmacy & Commerce. SKITM is NAAC Grade ‘A’ accredited & ISO Certified for its high quality of education. Shivajirao Kadam Group of Institutions are affiliated to RGPV, Bhopal & DAVV, Indore, approved by AICTE, PCI, BCI & Department of Higher Education MP. Through its industry aligned teaching pedagogy, the group has established itself as leader in education sector of Central India. The institute works on three key principles – Skill, Innovate and Transform. The institution aims to transform the lives of its students and establish itself as the centre of academic excellence in the state of Madhya Pradesh. With the unrivalled leadership and the guidance of eminent mentors, SKITM is changing the design and nature of education.

        Hosting schools offering programs such as:

        SHIVAJIRAO KADAM INSTITUTE OF TECHNOLOGY & MANAGEMENT
        FACULTY OF MANAGEMENT STUDIES – SKITM
        SHIVAJIRAO KADAM INSTITUTE OF PHARMACEUTICAL EDU. & RESEARCH
        TRANSNATIONAL SCHOOL OF LAW
        COLLEGE OF PROFESSIONAL STUDIES – ATC
        BHARATI VIDHYAPEETH SCHOOL OF PERFORMING ARTS (CENTRE)
        SKITM has emerged as the best institute in Central India.

        Accredited with Grade A, SKITM upholds the highest academic standards, ensuring the best in placement opportunities for its students. Under the unparalleled leadership, SKITM is changing the landscape of education, with an emphasis on extensive training sessions, a unique teaching methodology, strong collaborations, impactful certifications, and strategic partnerships.



        **directors message**
        Dear Students, Parents, Patrons and Stakeholders,

        It’s a pleasure to have you Explore us through this website.

        At SKITM, It’s our goal to enhance the employability of our graduates. We back our programs with research, a sound curriculum, intensive training and a host of Certifications. Our attitude of going beyond the books will surely position our graduates at the forefront of the Placement curve. Currently, SKITM is working extensively to bring its academic infrastructure at par with the best in the Industry.

        Besides, with the faculty actively engaged in academic research, we are committed to making SKITM a centre for an outstanding learning experience. The aim is not only to provide world class education but also to inculcate an attitude towards the betterment of society. We invite you to join us in our endeavor to create a knowledge based society that fortifies the intellectual, physical and mental dimensions of participating individuals. We produce graduates who have the skill, experience and confidence to be comfortable with the latest developments in their profession. In life you get out of, what you put in, and College life is no different. Dare to dream, put in the effort, enjoy the ride and reap the rewards!

        I need not to say that special care will be taken towards all the students in general and for those who are away from their homes in particular.

        I welcome you to discover SKITM. Let’s Make a Difference Together!

        Best Regards,

        Dr. Sanjay T Purkar

        Director

        SKITM




        About Our Chairman
        Prof. Shivajirao Kadam was born in a small village, realizing the significance of education for the transformation of an individual’s life, the parents of Prof. Dr. Kadam put a great deal of emphasis on his education. Dr. Shivajirao Kadam began life under extremely adverse circumstances and yet he rose to a position of pre-eminence in the field of education. Large volumes have been written about his illustrious journey. We are fortunate to be under his benevolent guidance.

        Dr. Kadam started his career as a lecturer in Bharati Vidyapeeth’s Yashwantrao Mohite College of Arts, Science and Commerce, after that he was appointed as the Principal of newly started Poona College of Pharmacy (Pune), which was then the first College of Pharmacy established within the jurisdiction of University of Pune. Dr. Kadam worked as the Principal of this College for the next 27 years till he became the Vice Chancellor of Bharati Vidyapeeth Deemed University, Pune in 2006. Under the visionary leadership of Dr. Kadam, the Poona College of Pharmacy made splendid strides in the areas of pharmacy education and research within a short time. This College subsequently became one of the leading pharmacy colleges in India. During his regime as the Principal, PG programs and subsequently Ph.D. programs in Pharmacy were launched in this College. He provided stimulus to the college faculty to undertake research projects of international standard. As a result, the college faculty has got 25 patents for their research projects and procedures. He is also credited with taking initiative and active interest in the area of Pharmacy at University of Pune, which led to the Establishment of Faculty of Pharmacy, University of Pune, the first of its kind to the State of Maharashtra.

        Having a genuine interest and zest for research, Dr. Kadam worked very hard to stimulate the research impulse of his colleagues. Many of them soon obtained research degrees and did substantive research, making this College known as a throbbing centre of pharmacy research. A large number of alumni of this College have occupied very important positions as members of teaching faculties, research scientists, pharmaceutical entrepreneurs, etc.

        Prof. Kadam has been involved in several leadership and administrative positions, which are a testament to his institution building abilities. His vast Administrative Experience includes his role as:-

        Chancellor, Bharati Vidyapeeth (Deemed to be University) Pune :15 June 2018 to Present
        Pro-Chancellor, Bharati Vidyapeeth University Pune :1 June 2017 to 14 June 2018
        Vice-Chancellor, Bharati Vidyapeeth Deemed University, Pune :5th Dec 2006 to 31st May
        Pro Vice-Chancellor, Bharati Vidyapeeth University, Pune :11 Years since (1996 to 2006)
        Secretary, Bharati Vidyapeeth University, Pune :(2000 to 2006)
        Principal, Poona College of Pharmacy : 27 Years (1979-2006)
        Dr. Kadam has been an active member and contributor to various Professional and Government bodies at National and International Levels. He has been a part of several illustrious and influential committees of the Government. He was a Member of the University Grants Commission, New Delhi for 6 years. He was a distinguished Member of the Pharmacy Council of India for 10 years where he has introduced ground breaking changes in the arena of India’s Pharmacy education. He was also a Member in the Governing Council of National Accreditation and Assessment Council (NAAC), Bangalore. He has contributed significantly as a Member of Finance Committees of both the UGC and NAAC. Besides, Dr. Kadam was a prominent member in various authorities of Pune University. He was a member of the University’s Executive Council, Academic Council and also of the Senate and Faculty of Pharmacy. It was with his initiative and efforts that a separate Faculty of Pharmacy was introduced in Pune University. It is considered as his significant achievement. He was also a member of the Standing Committee of University of Pune.

        Dr. Kadam was associated with Maharashtra State Board of Secondary and Higher Secondary Education, Pune. He has been also nominated by the University Grants Commission as Representative on the Boards of Management of several reputed institutions of higher education in India, viz., Narsee Monjee Institute of Management Studies, Mumbai, Kalinga Institute of Industrial technology (KIIT), Bhuvaneshwar, Govt. College of Engineering, Karad, Walchand College of Engineering, Sangli, etc. He also was on the Advisory Committees of Jaypee Institute of Information Technology, Noida and Karunya University, Coimbatore.

        Here’s a brief list of his Associations:-
        Dean, Faculty of Pharmaceutical Sciences, University of Pune : 09 Years
        Member, University Grants Commission, New Delhi : 6 years (Two Tenures) (2005-2011)
        Member, Governing Council, National Accreditation and Assessment Council (NAAC), Bangalore
        Member, Pharmacy Council of India : 10 years (2003-2013)
        Chairman,Bharati Sahakari Bank (Multi State Scheduled Bank) (5 Years)
        Chairman, Mahatma Gandhi Rugnalaya Charitable Hospital, Pune (From 1985 till date)
        Member, Executive Council/Management Council, University of Pune: 14 Years
        Member, Academic Council, University of Pune: 14 Years
        Member, Board of College & University Development, University of Pune: 10 Years
        Member, Senate, University of Pune: 16 Years
        Chairman, Board of Studies in Pharmaceutical Sciences, University of Pune: 13 Years
        Chairman, Statutes Committee, University of Pune: 06 years
        Chairman, Standing Committee, University of Pune: 06 Years
        Member, Board of Management, Narsee Monjee Institute of Management Studies, Mumbai
        Member, Board of Management, Kalinga Institute of Industrial Technology (KIIT), Bhuvaneshwar
        Member, Advisory Committee, Jaypee Institute of Information Technology, Noida
        Member, Advisory Committee, Karunya University, Coimbatore
        Chairman, Search committees for selection of Vice-Chancellors for various Universities.
        Awards, Honours, Distinctions Received by Prof. Kadam
        Received Bar Council of India “Golden Jubilee Special Award” on 16th February 2013 at Vigyan Bhavan New Delhi, for his invaluable contribution in the field of Higher Education in General and Legal Education in particular. Dr. Manmohan Singh, the Prime Minister of India was the Chief Guest and inaugurated the event. The celebrations witnessed the gracious presence of Hon’ble Dr. Ashwin Kumar, Union Minister of Law and Justice, Hon’ble G.Vahanvati, Attorney General of India and Shri Mannan Kumar Mishra, Chairman Bar Council of India. Hon’ble Mr.Justice Altamas Kabir, the Chief Justice of India presided over the function.
        Received a National Award at the hands of Smt.Pratibhatai Patil, then President of India, given in recognition of his contributions to the maintenance of the highest standards of higher education.
        “Best Teacher Award” Government of Maharashtra, January 2001.
        “Eminent Educationist, Administrator, Philanthropist and Researchist Award” (First Award) given by the Association of Pharmaceutical Teachers of India, Bangalore (2006) e) “Best Teacher Award” Government of Maharashtra, January 2001.
        “Pharmacy Educator of Distinction” Award, given by the Indian Pharmaceutical Association (2001).
        “Best Teacher Award” of Pune Municipal Corporation, 1993.
        “Samaj Bhushan Puraskar – 2012”
        Publications by Prof. Kadam:
        a) Books:

        Physical Pharmacy. (Published by Orient and Longman, Delhi.)
        Medicinal Chemistry,
        Principles of Medicinal Chemistry
        Maharashtra Universities Act, 1994
        b) Research Papers: Authored and published as many as 175 research papers in reputed international and national journals.

        Major Conferences/ Symposia Organized by Prof. Kadam
        Indian Pharmaceutical Congress, 2004 (Attended by 6000 delegates)
        All India Vice Chancellors Conference (2010)
        94th Annual Conference of Indian Economic Association (2011)
        International conference on Nano Science and Technology in 2010 & 2012.
        As a person, Dr. Kadam is very genial by nature. He has always been ready to help nature. He has a very wide circle of friends, well-wishers and followers. Among them are professionals of repute, social workers, artists, literary persons and others. He would never say no to give help to any deserving person or a cause. He is very closely associated with several philanthropic, social work, literary and other organizations. Through his innumerable achievements and contributions to society and education, Dr Shivajirao Kadam has reached such heights of eminence that mere words or articles are not enough to justify his work.





        Board of Governors

        Dr. Shivajirao Kadam, Chairman, BOG and Chancellor Bharti Vidyapeeth University, Pune

        Dr. DP Agrawal, Chairman Advisory Board and Former Chairman UPSC Board

        Mr. Siddharth Singh, Director, Emerald Heights School, Indore

        Dr. Piyush Trivedi, Fmr VC, RGPV, Bhopal | VF at Univ. of Toledo, USA| Dir. CITR coll. of pharmacy BVP, Pune

        Dr. Rakesh Saxena, Director, SGSITS

        Dr. KR Mahadik, Principal, Poona College of Pharmacy

        Dr. DK Jain, Principal, IPS Pharmacy

        Dr. DY Patil, Former Principal, IMSR-BVP, Navi Mumbai

        Nominee of RGPV

        Nominee of DTE

        Nominee of Government of MP

        Nominee of DAVV

        Nominee of AICTE




        Board of Advisors

        Dr. DP Agrawal, Former Chairman, UPSC

        Shri Sewaram, Retd. IAS, Former Principal Secretary, Govt. of MP

        Shri Sunil Choradia, MD, Raj Ratan Wires

        Dr. DN Reddy, Former Vice Chancellor JNTU Hyderabad

        Dr. Piyush Trivedi, Fmr VC, RGPV, Bhopal | VF at Univ. of Toledo, USA| Dir. CITR coll. of pharmacy BVP, Pune

        Dr. KR Mahadik, Principal, Poona College of Pharmacy

        Dr. Charles R. Ashby, Jr. Professor, St. John's University, New York (USA)

        Ms. Maria Isabel Veiga, Researcher Academic, University of Minho, Portugal

        Dr. Hoyun Lee, Professor & Sr. Scientist, Northern Ontario School of Medicine

        Dr. Amit Tiwari, Professor & Scientist, University of Toledo (USA)

        Dr. Rakesh Saxena – Director, SGSITS

        Mr. Siddharth Singh, Director, Emerald Heights School, Indore

        Mr. Sanjeev Pendharkar, Managing Director at Vicco Laboratories

        Mr. Manoj Jain – MD & CEO, Shriram Life Insurance

        Mr. Amit Kumat - MD and CEO, Prataap Snacks (Yellow Diamond)

        Mr. Hemant Dande, President & COO, Raptakos, Brett & Co Ltd

        Shri Sanjay Jagdale, Former Secretary, BCCI

        Mr. Amit Rawat, Lead, AWS Institute Amazon Web Services (AWS), Sydney, Australia

        Mr. Libi Bhaskaran, General Manager, IBM India

        Shri Sushil Doshi, Padamshri Awardee, Indian Cricket Commentator

        Mr. Sandeep Pagere, President – Road, Highways & Bridges, Choice Consultancy Services Ltd.

        Mr. Pankaj Khapra, Head, F&D and Clinical Affairs, Alembic Pharmaceuticals

        Mr. Mayank Nagar, Vice President, Dr. Reddys USA

        Ms. Aastha Billore, Executive Director, Arab Media Group (Dubai Holding)

        Dr. Rakesh Taran, Leading Oncologist & Philanthropist

        Ms. Akshata Trivedi, Sr. Program Manager, Salesforce





        Our Partners
        Our partnerships and collaborations are helping us build a more vibrant changemaker ecosystem in our institute and push forward SKITM’s vision for a better future.

        We are excited to partner with many wonderful National and International Organizations to offer our students the strongest educational experience and best employment opportunities.

        MOU University of Toledo, USA
        Cooperative memorandum of understanding between Shivajirao Kadam institute of technology and management, Indore and University of Toledo, USA.

        Campbellsville University, Kentucky, USA
        Cooperative memorandum of understanding between Shivajirao Kadam institute of technology and management, Indore and Campbellsville University, Kentucky, USA.

        MOU Data Flair and SKITM
        Cooperative memorandum of understanding between Shivajirao Kadam institute of technology and management, Indore and DataFlair Web Services Pvt Ltd, Indore.

        Certificate of Establishment IIC
        Translational Kowledge Society’s Group Indore has established an Institution’s Innovation Cell, Ministry of Education, Govt. of India during the academic calendar year 2020-21.

        Red Hat Academy
        Red Hat, a recognized leader in open source, provides educational institutions with high-quality curriculum for teaching core open source technologies through the Red Hat Academy program. 82% of companies using online job boards to recruit for Linux positions request Red Hat Certified Professionals. Red Hat’s quality curriculum keeps pace with rapidly-changing open source technologies. Red Hat Academy provides curriculum to institutions based on open source solutions covering the Linux operating system, cloud computing using OpenStack, and big data-driven web portals using Red Hat JBoss Middleware.

        Virtual Lab
        Virtual Labs project is an initiative of Ministry of Human Resource Development (MHRD), Government of India under the aegis of National Mission on Education through Information and Communication Technology (NMEICT). This project is a consortium activity of twelve participating institutes and IIT Delhi is coordinating institute. It is a paradigm shift in ICT-based education. For the first time, such an initiative has been taken-up in remote‐experimentation. Under Virtual Labs project, over 100 Virtual Labs consisting of approximately 700+ web-enabled experiments were designed for remote-operation and viewing.

        Spoken Tutorial
        The Spoken Tutorial project is funded and developed by the NMEICT, IIT Bombay and launched by the Ministry of Education (MoE), Government of India.

        The aim of spoken tutorials is to popularize E-learning.
        It is coordinated through ICT based system. Spoken Tutorial is an audio-video educational content platform. Here one can learn various Free and Open Source Software all by oneself.

        UiPath
        RPA has provided an excellent solution for organizations to replace repetitive, mundane, rule-based processes with software bots. It is now helping organizations who were looking to increase their workflow accuracy and efficiency. First, RPA was widely adopted in the IT sector. It amazed many big organizations as well as small and medium enterprises with outstanding results. Later, it was adopted in other sectors like Finance, Accounting, Banking, etc.

        AWS Academy
        AWS Academy provides higher education institutions with a free, ready-to-teach cloud computing curriculum that prepares students to pursue industry-recognized certifications and in-demand cloud jobs. Our curriculum helps educators stay at the forefront of AWS Cloud innovation so that they can equip students with the skills they need to get hired in one of the fastest-growing industries.

        Coursera
        Coursera partners with more than 200 leading universities and companies to bring flexible, affordable, job-relevant online learning to individuals and organizations worldwide. We offer a range of learning opportunities—from hands-on projects and courses to job-ready certificates and degree programs.

        EC-Council Academia
        Students will have the opportunity to achieve industry recognized certifications and compete in free cyber competitions as they complete their degree programs, achieving the ultimate stackable credential lineup to enhance their resume.

        Oracle Academy
        Oracle Academy membership offers educational institutions and educators free computing education resources for the classroom to help increase knowledge, skills development, innovation, and diversity in technology fields.

        GirlScript
        GirlScript is the fastest growing tech-community in India. It is a non-profit project brought to you by GirlScript Foundation to help beginners in technology.



        Leadership Team
        The leadership team at SKITM is committed to upholding and promoting the mission of the School: educate and develop innovative, entrepreneurial and responsible business leaders.

        With their diverse backgrounds and perspectives, the Board of Governors, the Advisory Body and the Director work together to take the institute forward, supporting the faculty and staff, spearheading a host of new academic projects and initiatives across its campuses and around the globe, and building and sustaining the collaborative, inclusive environment for students that encourages learning and invention.


        Dr. Shivajirao Kadam, Chairman, BOG and Chancellor Bharti Vidyapeeth University, Pune

        Dr. Rahul Kadam, Chairman, Transnational Knowledge Society and MD, Udagiri Sugar Limited

        Dr. DP Agrawal, Chairman Advisory Board and Former Chairman UPSC Board

        Dr. Ashok Kumat, Vice Chairman, SKITM

        Dr. Sanjay Purkar, Director, SKITM

        Prof. Satish B. Purohit, Dean Innovations, Former Professor Mechanical Engineering, SGSITS

        Shri Sanjay Jagdale, Director, Sports and Former BCCI Secretary

        Dr. Rizwan Khan, Principal, SKIPER

        Dr. Sumeet Khurana, Director, Faculty of Management Studies

        Dr. Vishal Mehta, Principal, College of Professional Studies

        AVM Praveen Kumar (Retd.) AVSM, VSM, Dean Student Affairs

        Dr. Preetesh Purohit, Professor and Dean Engineering

        Dr. Rashmi Yadav, Head, Computer Science & Engineering

        Dr. Amit Udawat, Head, Electronics & Communication

        Prof. Girish Patidar, Head, Civil Engineering




        The Society
        Transnational Knowledge Society was founded in the year 2008. The aim of the society is to elevate the region by providing high-quality education at reasonable costs. Till now, society has catered to over 8000 students, transforming their lives and the lives of their families. Transnational Knowledge Society has been instrumental in improving the educational standards in the city by setting an example of good governance and a student-centric approach. In the past, the society has controlled the Transnational Knowledge Society Group of Institutions and later on the Acropolis Technical Campus. Currently, there are 4 Colleges under its aegis, catering to over 1700 students from across the State. Transnational Knowledge Society through SKITM aims to impart highly impactful education, which helps students build successful careers. High focus on the moral compass, societal transformation, and the good of the industry are the messages which resonate in its teachings.





        Vision and Mission
        Vision
        Holistic development of the learner through excellence in education, innovation & research.

        Mission
        To create a competitive and technically empowered environment which enables students to develop and discover their potential and become competent to address industrial, societal and global challenges.
        To achieve academic excellence in application oriented research, novelty and creativity leading to emergence of technocrats, leaders, innovators and renowned entrepreneurs.
        To become a top school in the country where students are raised with Holistic learning for inculcating core values of professionalism, gender equality, transparency and ethics.
        To establish partnership with globally recognized institutions and organizations to foster students with industrial exposure through extensive hands-on training.
        To ensure overall nurturing and all round personality development of students by continuous monitoring and guidance.
        Quality Policy
        We are committed to develop high quality, professionally groomed technocrats and human resources to serve the nation through standards of excellence in academics, governance, research, innovation, training and infrastructure and to remain accountable for quality education through self-evaluation, regular monitoring and implementing corrective actions in an ethical and transparent manner.
        ''')

    promt = 'You are an ai chatbot and you have to answer some question **You can answer them using the above paragraph of information**, the Questions Start from here => \n'
    response = chat_session.send_message(f" paragraph of information ({prompt})\n\n {promt}\n {text_input}")

    return str(response.text)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('message')
    try:
        response_text = run(user_input)  # Pass the API key here
        return jsonify({"response": response_text})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
