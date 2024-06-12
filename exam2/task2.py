from bs4 import BeautifulSoup

# Read the HTML file
with open("phases_soften.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Define the titles for each phase
phase_titles = {
    "Deployment": "This is where the application or software is created.",
    "Development": "Decomposition of major system components into program units.",
    "Monitoring": "The planning of objectives, risk analysis, engineering or development, and finally review.",
    "Testing": "Phase 1: Planning\n\nThe initial stage of software development, Planning, involves defining the software’s purpose and scope, much like pinpointing our destination and plotting the best route."
}

# Extract and display the titles and first paragraphs
for phase, description in phase_titles.items():
    print(f"{phase}:\n\n{description}\n")
    # Find the next paragraph element after the title
    h2_tag = soup.find("h2", string=phase)
    if h2_tag:
        next_paragraph = h2_tag.find_next("p")
        if next_paragraph:
            print(next_paragraph.get_text())
    else:
        print(f"No h2 tag found for phase: {phase}")
    print("\n---\n")  # Separator between phases