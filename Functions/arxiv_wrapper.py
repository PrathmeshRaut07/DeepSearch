import arxiv
import os
base_directory = os.getcwd()  # Gets the absolute path of the current working directory
temp_directory = os.path.join(base_directory, "temp")  # Creates absolute path for "temp" folder
def download_top_pdfs(query, num_results=3):
    search = arxiv.Search(
        query=query,
        max_results=num_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    for result in search.results():
        # print(f"Title: {result.title}")
        
        # author_names = [author.name for author in result.authors]
        # print(f"Authors: {', '.join(author_names)}")
        
        # print(f"Published: {result.published}")
        # print(f"Summary: {result.summary}\n")
        result.download_pdf(dirpath=temp_directory)
        print(f"Downloaded PDF: {result.pdf_url}\n")
download_top_pdfs("Convolution Layers")