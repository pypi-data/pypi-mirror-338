#!/usr/bin/env python
"""
APIRotater Setup Tool - Helps you set up your API keys

This script will:
1. Create a .env file in your home directory
2. Guide you through adding your API keys
"""

import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="Setup API keys for APIRotater")
    
    parser.add_argument(
        "--location", "-l", 
        choices=["current", "home"],
        default="current",
        help="Where to create the .env file: 'current' for current directory, 'home' for home directory"
    )
    args = parser.parse_args()
    
    # Determine the location to create the .env file
    if args.location == "home":
        env_path = os.path.join(os.path.expanduser("~"), ".apirotater.env")
        location_description = "home directory"
    else:
        env_path = os.path.join(os.getcwd(), ".env")
        location_description = "current directory"
    
    print(f"APIRotater Setup Tool")
    print(f"====================")
    print(f"Setting up your API keys in {location_description} ({env_path})")
    
    # Check if the file already exists
    if os.path.exists(env_path):
        answer = input(f"A .env file already exists at {env_path}. Add to it? (y/n): ")
        if answer.lower() != "y":
            print("Setup cancelled. Existing .env file was not modified.")
            return
    
    # Get user's API keys
    api_keys = []
    
    # First ask for common API keys
    common_keys = {
        "GOOGLE_API_KEY": "Google API Key (for Gemini, etc.)",
        "OPENAI_API_KEY": "OpenAI API Key",
    }
    
    for key_name, description in common_keys.items():
        value = input(f"\n{description} (press enter to skip): ")
        if value.strip():
            api_keys.append((key_name, value))
    
    # Now ask for generic API keys
    print("\nYou can add more API keys. These will be used in rotation.")
    
    key_num = 1
    while True:
        key_name = f"API_KEY_{key_num}"
        value = input(f"\nAPI Key {key_num} (press enter to finish): ")
        if not value.strip():
            break
        
        api_keys.append((key_name, value))
        key_num += 1
    
    if not api_keys:
        print("No API keys provided. Setup cancelled.")
        return
    
    # Create or update the .env file
    mode = "a" if os.path.exists(env_path) else "w"
    with open(env_path, mode) as f:
        # Add a header if we're creating a new file
        if mode == "w":
            f.write("# APIRotater environment file\n")
            f.write("# Contains API keys used by APIRotater\n\n")
        else:
            f.write("\n# Added by APIRotater setup tool\n")
        
        for key_name, value in api_keys:
            f.write(f"{key_name}={value}\n")
    
    print(f"\nSuccess! {len(api_keys)} API keys were saved to {env_path}")
    print("You can now use APIRotater in your projects:")
    print("\nimport apirotater")
    print("api_key = apirotater.key()")
    
if __name__ == "__main__":
    main() 