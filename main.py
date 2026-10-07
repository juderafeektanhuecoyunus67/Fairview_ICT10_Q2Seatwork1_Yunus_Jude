from pyscript import document, display

# Official list of ICT club members, stored lowercase for case-insensitive matching
club_members = [
    "marco zambales",
    "george orwell",
    "kevin xin",
    "john doe",
    "roy cruz",
    "jude yunus",
]


def verify_candidate(event):
    """
    Retrieves first and last name from the DOM, verifies membership against list,
    and displays result in the top banner using a dictionary mapping
    without using any conditional statements or loops.
    """
    # Step 1 -> Retrieve and combine the candidate's first and last names
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("Last_name").value.strip()
    candidate_name = f"{first_name} {last_name}".strip()

    # Step 2 -> Testing the membership in club list (returns True or False) 
    is_member = candidate_name.casefold() in club_members

    # Step 3 -> Map boolean outcome directly to required output strings
    status_messages = {
        True: f"✅ Success! Congratulations {candidate_name}! You are officially part of the ICT club.",
        False: f"❌ Sorry {candidate_name}, your name is not on the list."
    }

    # Step 4 -> Extract corresponding status message via boolean key lookup
    result_text = status_messages[is_member]

    # Step 5 -> Update the DOM banner element with the result text
    output_element = document.getElementById("output1")
    output_element.innerText = ""
    display(result_text, target="output1")

    # For success verification, input names such as "MARCO ZAMBALES" or "George Orwell".