import os
from dotenv import load_dotenv
from langchain_community.tools import TavilySearchResults

def search_tavily(query: str, max_results: int = 5, 
                   include_answer: bool = True, 
                   include_raw_content: bool = True, 
                   include_images: bool = True) -> dict:
    """
    Search Tavily using the provided query and return the response.

    Parameters:
        query (str): The search query.
        max_results (int): Maximum number of search results to retrieve.
        include_answer (bool): Whether to include answers in the result.
        include_raw_content (bool): Whether to include raw content in the result.
        include_images (bool): Whether to include images in the result.

    Returns:
        dict: The response from TavilySearchResults.
    """
    # Load environment variables from a .env file
    load_dotenv()
    os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

    # Initialize the Tavily search tool with the specified parameters
    tool = TavilySearchResults(
        max_results=max_results,
        include_answer=include_answer,
        include_raw_content=include_raw_content,
        include_images=include_images,
    )

    # Invoke the tool with the search query and return the response
    response = tool.invoke({'query': query})
    return response
