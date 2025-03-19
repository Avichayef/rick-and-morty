# Required libraries
import requests  # For making HTTP requests to the API
import csv      # For writing data to CSV files

def get_all_characters():
    """
    Fetches all characters from the Rick and Morty API.
    
    This function handles pagination and collects all characters across all pages.
    It makes multiple API requests until there are no more pages to fetch.
    
    Returns:
        list: A list of dictionaries containing character information
    """
    # Initialize empty list to store all characters
    characters = []
    
    # Start with the first page
    page = 1
    
    # API endpoint URL
    base_url = "https://rickandmortyapi.com/api/character"
    
    # Continue fetching until we've got all pages
    while True:
        # Make API request for current page
        response = requests.get(f"{base_url}?page={page}")
        # Convert response to JSON format
        data = response.json()
        
        # Check if the API request was successful
        if response.status_code != 200:
            print("Error fetching data from API")
            break
        
        # Add characters from current page to our list
        characters.extend(data['results'])
        
        # Check if there are more pages to fetch
        if not data.get('info').get('next'):
            break
            
        # Move to next page
        page += 1
    
    return characters

# ---------------------------------------------------------------------------------------------------------

def filter_characters(characters):
    """
    Filters the characters based on specific conditions:
    - Species must be Human
    - Status must be Alive
    - Origin must be Earth
    
    Args:
        characters (list): List of character dictionaries from the API
        
    Returns:
        list: Filtered list containing only characters matching all conditions
    """
    # Create empty list for filtered characters
    filtered_characters = []
    
    # Check each character
    for character in characters:
        # Check if character meets ALL conditions
        if (character['species'] == 'Human' and 
            character['status'] == 'Alive' and 
            'Earth' in character['origin']['name']):
            
            # Create a simplified character dictionary with only the info we need
            filtered_char = {
                'name': character['name'],
                'location': character['location']['name'],
                'image': character['image']
            }
            # Add the filtered character to our list
            filtered_characters.append(filtered_char)
    
    return filtered_characters

# ---------------------------------------------------------------------------------------------------------

def save_to_csv(characters, filename="rick_morty_humans.csv"):
    """
    Saves the filtered characters to a CSV file.
    
    Args:
        characters (list): List of filtered character dictionaries
        filename (str): Name of the CSV file to create (default: rick_morty_humans.csv)
    """
    # Define the column headers for our CSV
    headers = ['name', 'location', 'image']
    
    # Open the file in write mode
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        # Create a CSV writer object
        writer = csv.DictWriter(file, fieldnames=headers)
        
        # Write the headers to the CSV file
        writer.writeheader()
        
        # Write each character's data as a row
        writer.writerows(characters)

# ---------------------------------------------------------------------------------------------------------

def main():
    """
    Main function to run the entire process:
    1. Fetch all characters
    2. Filter them based on conditions
    3. Save results to CSV
    """
    print("Starting to fetch characters...")
    all_characters = get_all_characters()
    print(f"Found {len(all_characters)} total characters")
    
    print("Filtering characters...")
    filtered_characters = filter_characters(all_characters)
    print(f"Found {len(filtered_characters)} humans from Earth who are alive")
    
    print("Saving to CSV...")
    save_to_csv(filtered_characters)
    print("Done! Check rick_morty_humans.csv for results")

# Run the program
if __name__ == "__main__":
    main()
