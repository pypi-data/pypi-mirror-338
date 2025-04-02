class Resume:
    def __init__(self):
        self.name = "Sonu Kr Sahani"
        self.title = "Coder & Gamer"
        self.contact = {
            "📧 Email": "sahanix7@gmail.com",
            "📞 Phone": "+91 9123741694",
            "🌐 LinkedIn": "linkedin.com/in/sonusahani",
            "🐍 GitHub": "github.com/sonusahani"
        }
        
        self.summary = (
            "👋 Hi! I'm Sonu, a passionate Python developer with expertise in data structures, "
            "game development, and automation. I also develop games like RPGs and VNs. "
            "I love building interactive applications, anime-inspired projects, and automation tools."
        )
        
        self.skills = [
            "Python", "Data Structures & Algorithms", "Game Development", "AI & Automation", 
            "JavaScript", "RPG Maker MV", "Unity", "Godot", "Flask", "Pandas", "Tally ERP", "NumPy"
        ]
        
        self.experience = [
            {
                "Position": "WordPress Developer & SEO",
                "Company": "Seven Destination",
                "Duration": "2022 - Present",
                "Responsibilities": [
                    "📌 Developed website and managed travel bookings & transactions in Tally ERP."
                ]
            },
            {
                "Position": "Indie Game Developer",
                "Company": "Freelance",
                "Duration": "2021 - Present",
                "Responsibilities": [
                    "🎮 Developed an anime-style RPG named Tarang.",
                    "🎮 Created quests based on the *Ramayana*, integrating puzzles and NPC interactions.",
                    "🎮 Built an RPG Maker MV game where players explore UNESCO heritage sites in India.",
                    "🎮 Designed combat mechanics and item systems for an immersive gameplay experience."
                ]
            }
        ]
        
        self.education = {
            "Degree": "B.Com",
            "University": "Calcutta University",
            "Year": "2020 - 2025"
        }

        self.projects = [
            {
                "Name": "Tarang for Waves Game Jam",
                "Description": "Developed an RPG where players explore and complete quests.",
                "Technologies": ["JavaScript", "RPG Maker MV", "Krita"]
            }
        ]

    def show_contact(self):
        print("\n📞 CONTACT DETAILS\n" + "-"*30)
        for key, value in self.contact.items():
            print(f"{key}: {value}")

    def show_summary(self):
        print("\n📌 SUMMARY\n" + "-"*30)
        print(self.summary)

    def show_skills(self):
        print("\n💡 SKILLS\n" + "-"*30)
        print(", ".join(self.skills))

    def show_experience(self):
        print("\n💼 EXPERIENCE\n" + "-"*30)
        for job in self.experience:
            print(f"\n🔹 {job['Position']} at {job['Company']} ({job['Duration']})")
            for responsibility in job["Responsibilities"]:
                print(f"   ➤ {responsibility}")

    def show_education(self):
        print("\n🎓 EDUCATION\n" + "-"*30)
        for key, value in self.education.items():
            print(f"{key}: {value}")

    def show_projects(self):
        print("\n📂 PROJECTS\n" + "-"*30)
        for project in self.projects:
            print(f"\n🔹 {project['Name']}")
            print(f"   📌 {project['Description']}")
            print(f"   🔧 Technologies: {', '.join(project['Technologies'])}")

    def show(self):
        print(f"\n🎯 {self.name} - {self.title}\n" + "="*40)
        self.show_contact()
        self.show_summary()
        self.show_skills()
        self.show_experience()
        self.show_education()
        self.show_projects()


def show():
    resume = Resume()
    resume.show()


def interactive():
    resume = Resume()
    while True:
        print("\n🔹 Choose a section to view:")
        print("1️⃣ Contact Details")
        print("2️⃣ Summary")
        print("3️⃣ Skills")
        print("4️⃣ Experience")
        print("5️⃣ Education")
        print("6️⃣ Projects")
        print("7️⃣ Show Full Resume")
        print("0️⃣ Exit")

        choice = input("\nEnter choice (0-7): ")
        
        if choice == "1":
            resume.show_contact()
        elif choice == "2":
            resume.show_summary()
        elif choice == "3":
            resume.show_skills()
        elif choice == "4":
            resume.show_experience()
        elif choice == "5":
            resume.show_education()
        elif choice == "6":
            resume.show_projects()
        elif choice == "7":
            resume.show()
        elif choice == "0":
            print("\n👋 Exiting Resume Viewer...")
            break
        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    interactive()
