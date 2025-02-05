import arxiv

def download_top_pdfs(query, num_results=3):
    # Search for articles on arXiv
    search = arxiv.Search(
        query=query,
        max_results=num_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    # Iterate through the results and download PDFs
    for result in search.results():
        print(f"Title: {result.title}")
        
        # Extract author names from the Author objects
        author_names = [author.name for author in result.authors]
        print(f"Authors: {', '.join(author_names)}")
        
        print(f"Published: {result.published}")
        print(f"Summary: {result.summary}\n")
        
        # Download the PDF
        result.download_pdf()
        print(f"Downloaded PDF: {result.pdf_url}\n")

# Example usage
download_top_pdfs("machine learning")