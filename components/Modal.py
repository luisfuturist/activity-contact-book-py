def Modal(title, content):
    # Define the width of the modal
    width = max(len(line) for line in content) + 4

    print('+' + '-' * width + '+') # Draw the top border    
    print(f"| {title.center(width)} |") # Print the title
    print('+' + '-' * width + '+') # Draw a separator

    # Print the content inside the modal
    for line in content:
        print(f"| {line.center(width)} |")

    print('+' + '-' * width + '+') # Draw the bottom border