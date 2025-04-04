from mcp.server.fastmcp import FastMCP
import requests
from bs4 import BeautifulSoup

mcp = FastMCP("WebExtractor")

@mcp.tool()
def extract_content(url: str) -> str:
    """Extract content from a URL
    
    Args:
        url: The URL to extract content from
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove scripts and styles
        for tag in soup(['script', 'style']):
            tag.decompose()
            
        # Get text
        text = soup.get_text()
        
        # Clean up whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return text
        
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    """Entry point for the command-line script"""
    mcp.run()

if __name__ == "__main__":
    main()