import tensorflow_hub as hub
import numpy as np
from test_2_data_set import fruits_dict, blog_posts, travel_dict

embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

def main():
    lists: list[Post] = []
    while True:
        try:
            print("Choices:")
            print("1: Add a value")
            print("2: List the value")
            print("3: Semantic Searching")
            print("4: Append all fruits")
            print("5: Append all blogs")
            print("6: Append all travel loc")
            print("7: Append long essay")
            print("8: Clear List")
            print("9: Exit")
            choice = int(input("What do you want to do: "))
            match (choice):
                case 1:
                    add_data(lists)
                case 2:
                    list_data(lists)
                case 3:
                    search_data(lists)
                case 4:
                    append_all_fruits(lists)
                case 5:
                    append_all_blog(lists)
                case 6:
                    append_all_travel(lists)
                case 7:
                    add_long_essay(lists)
                case 8:
                    lists.clear()
                case 9:
                    break
                case _:
                    print("Please choose within the number")
        except Exception as e:
            print("Please enter a valid choice")
            print(e)
            continue

def add_data(lists: list):
    print()
    title = input("Enter the title: ")
    content = input("Enter the content: ")

    embedding_vector = get_embedding(content)
    post = Post(title=title, content=content, embedding=embedding_vector)

    lists.append(post)

    print("Added data\n")

def list_data(lists: list):
    print()
    print("Lists of fruits you have:")
    for i in lists:
        print(i.title, end=", ")
    print("\n")

def append_all_fruits(lists: list):
    print()
    for i in fruits_dict:
        embedding_vector = get_embedding(i.get("content"))
        post = Post(title=i.get("title"), content=i.get("content"), embedding=embedding_vector)

        lists.append(post)
    print("Appended all\n")

def append_all_blog(lists: list):
    print()
    for i in blog_posts:
        embedding_vector = get_embedding(i.get("content"))
        post = Post(title=i.get("title"), content=i.get("content"), embedding=embedding_vector)

        lists.append(post)
    print("Appended all\n")

def append_all_travel(lists: list):
    print()
    for i in travel_dict:
        embedding_vector = get_embedding(i.get("content"))
        post = Post(title=i.get("title"), content=i.get("content"), embedding=embedding_vector)

        lists.append(post)
    print("Appended all\n")

def add_long_essay(lists: list):
    title = "The Impact of Artificial Intelligence on Education"
    content = "Artificial Intelligence (AI) has emerged as one of the most transformative forces of the 21st century. While its influence extends across healthcare, finance, transportation, and countless other sectors, one of the most profound areas of impact is education. Education is the foundation of societal progress, and any tool that reshapes how individuals learn, teach, and engage with knowledge has lasting consequences. AI is no longer an abstract concept confined to research labs; it has become a practical, everyday technology that changes classrooms, online platforms, and even informal learning environments. This essay explores the role of AI in education, the opportunities it creates, the challenges it introduces, and its potential future implications. AI as a Personalized Learning Tool Traditional education often struggles with a one-size-fits-all model. In large classrooms, it is difficult for teachers to adapt lessons to the varied needs of students. Some learners grasp material quickly, while others require more time and alternative explanations. AI has shown promise in solving this issue through personalized learning systems. Adaptive learning platforms use algorithms to analyze a student’s performance and adjust content accordingly. For instance, if a student struggles with algebraic equations, the system can provide additional practice problems, step-by-step hints, and even video explanations until mastery is achieved. Conversely, advanced learners can be challenged with more complex material rather than being forced to wait for the rest of the class. The benefit of personalization extends beyond academic progress. When students feel that the content matches their abilities and learning style, they are more engaged and motivated. AI systems can detect when learners become disengaged and adjust the pace or format of delivery. This type of customization was once a dream in traditional education, but AI makes it scalable and accessible. AI-Powered Tutoring and Support Another significant contribution of AI is in the field of tutoring. Intelligent tutoring systems provide students with on-demand help outside regular school hours. Unlike human tutors, AI-driven systems are available 24/7, making education more accessible to learners across time zones and socioeconomic backgrounds. These systems not only explain concepts but can also identify misconceptions in real time. For example, if a student repeatedly makes the same mistake in solving quadratic equations, the AI tutor can recognize the pattern and provide targeted feedback. Language learning has also been revolutionized through AI. Apps powered by natural language processing allow students to practice speaking, listening, and writing with immediate correction. This form of interactive tutoring would have been extremely expensive in the past but is now available to anyone with a smartphone. Administrative Efficiency and Teacher Support AI’s role in education is not limited to students. Teachers and administrators also benefit from the automation of repetitive tasks. Grading assignments, scheduling lessons, analyzing test performance, and generating reports consume significant time. AI tools can take over these administrative responsibilities, allowing educators to focus more on pedagogy and human interaction. Automated grading of multiple-choice and even short-answer questions has already become common, and advances in natural language processing may soon allow AI to assess essays with near-human accuracy. Additionally, AI can provide teachers with insights into student progress. By analyzing data across multiple students, algorithms can highlight common problem areas. Teachers can then adjust lesson plans, dedicate extra sessions to challenging topics, or provide specialized support for struggling learners. Far from replacing teachers, AI enhances their effectiveness by equipping them with actionable insights. Challenges and Ethical Concerns Despite its many advantages, the integration of AI in education is not without challenges. One concern is data privacy. AI systems require large amounts of student data to function effectively. This includes academic records, behavioral data, and sometimes even voice or facial recognition. If not handled responsibly, such information could be misused or compromised in data breaches. Schools and institutions must establish strong ethical standards and safeguard mechanisms to protect learners. Another challenge is the risk of overreliance on technology. While AI can provide personalized support, it cannot replace the empathy, mentorship, and moral guidance of human teachers. Education is not solely about transferring knowledge; it is also about fostering creativity, collaboration, and social skills. AI systems, at least for now, lack the emotional intelligence to nurture these human qualities. Equity is also a pressing concern. Although AI promises to make education more accessible, it can also widen the digital divide. Students in wealthy regions may benefit from advanced AI tools, while those in underdeveloped areas may struggle to access even basic internet connectivity. Policymakers and educators must work to ensure that AI does not become a tool that reinforces inequality but instead serves as a bridge toward inclusivity. The Future of AI in Education Looking ahead, the role of AI in education will likely expand even further. Virtual reality combined with AI could create immersive learning environments where students explore historical events or conduct science experiments in simulated laboratories. AI-driven career counseling tools might analyze student skills and recommend personalized career paths, internships, or training programs. Collaborative AI platforms could also connect learners from across the globe, enabling cultural exchange and cross-border teamwork. However, the key to AI’s successful integration lies in balance. The technology should complement, not replace, the human aspects of education. Teachers will continue to play an irreplaceable role as mentors, motivators, and role models. AI should serve as a powerful assistant, amplifying human strengths while addressing systemic weaknesses. Conclusion Artificial Intelligence has already begun reshaping education in ways that were unimaginable a generation ago. From personalized learning pathways to intelligent tutoring systems and administrative support, AI is opening doors to more efficient, engaging, and inclusive education. At the same time, it raises important ethical questions regarding privacy, equity, and the role of human educators. The future of education will likely be a hybrid model, blending the efficiency of AI with the compassion and creativity of humans. If implemented responsibly, AI has the potential to democratize education and prepare learners for the complex challenges of the modern world."
    embedding_vector = get_embedding(content)
    post = Post(title=title, content=content, embedding=embedding_vector)

    lists.append(post)

    print("Added data\n")

def get_embedding(text, as_lsit=True):
    vec = embed([text])[0].numpy()  # 512-dim vector
    return vec.tolist() if as_lsit else vec

def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def search_data(lists: list):
    print()
    query = input("Enter query: ")

    query_vec = get_embedding(query)

    results = []
    for doc in lists:
        sim = cosine_similarity(query_vec, doc.embedding)
        results.append({ "id": doc.id,"title": doc.title, 
                        "content": doc.content, "score": float(sim)})
    
    results.sort(key=lambda x: x["score"], reverse=True)

    print(f"You have search for: {query}")
    for i in results[:5]:
        print(f"{i.get("title")}")

    print()

class Post:
    counter: int = 0

    def __init__(self, title: str, content: str, embedding):
        Post.counter += 1
        self.id = Post.counter
        self.title = title
        self.content = content
        self.embedding = embedding

main()  