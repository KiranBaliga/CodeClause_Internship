import hashlib
import base64

# Function to generate a short URL
def create_short_link(long_url):
    # Create a hash of the long URL
    url_hash = hashlib.md5(long_url.encode())
    # Convert the hash to a base64 encoded string
    encoded_hash = base64.urlsafe_b64encode(url_hash.digest()).decode()[:6]
    # Return the shortened URL
    return f"http://short.link/{encoded_hash}"

# Function to get a long URL from the user and print the shortened URL
def main():
    original_url = input("Enter your long URL to shorten: ")
    short_link = create_short_link(original_url)
    print(f"Your shortened link: {short_link}")

if __name__ == "__main__":
    main()
