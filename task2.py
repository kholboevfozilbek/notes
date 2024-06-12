from bs4 import BeautifulSoup

# Read the HTML file
with open('phases_soften.html', 'r') as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Choose the title for each phase from the list
titles = ['Deployment', 'Development', 'Monitoring', 'Testing']

# Initialize phase counter
i = 1

# Iterate over the titles and find the corresponding elements
for title in titles:
    # Find the element with the specified title
    phase_title = soup.find('h2', string=title)
    
    if phase_title:
        # Find the next paragraph element after the title
        next_paragraph = phase_title.find_next('p')
        
        if next_paragraph:
            # Print phase number, title, and paragraph
            print(f'Phase {i}: {title}\n')
            print(next_paragraph.text)
            print('\n')
        
        # Increment phase counter
        i += 1