import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor


# Function to send POST request asynchronously
async def send_post_request(session, url, payload, headers, context):
    try:
        async with session.post(url, json=payload, headers=headers) as response:
            if response.status == 200:
                response_data = await response.json()
                generated_deck_url = response_data.get("url")
                return context, generated_deck_url
            else:
                return (
                    context,
                    f"Failed to generate deck. Status code: {response.status}, Response: {await response.text()}")
    except Exception as e:
        return (context, f"An error occurred: {str(e)}")


# Function to process multiple JSON payloads synchronously with concurrency
def process_multiple_jsons(json_list):
    url = "https://deck-generator.onrender.com/api/generate-decks"
    headers = {
        "Content-Type": "application/json",
    }

    # Wrapper function to run async tasks in threads
    def run_in_thread(payload, context):
        async def send_request():
            async with aiohttp.ClientSession() as session:
                return await send_post_request(session, url, payload, headers, context)

        return asyncio.run(send_request())

    # Use ThreadPoolExecutor to execute async tasks concurrently
    with ThreadPoolExecutor() as executor:
        tasks = []
        for i, payload in enumerate(json_list):
            context = f"Response {i + 1}"
            tasks.append(executor.submit(run_in_thread, payload, context))

        # Gather the results
        results = [task.result() for task in tasks]
        return results


# Example usage
if __name__ == "__main__":
    json_list = [
        {
            "hypothesis": "Sundai Club has the potential to expand its influence and effectiveness by forming strategic partnerships with local businesses, thereby enhancing opportunities for mentorship, internships, and real-world experience.",
            "pain_point": "Students often seek mentorship and internship opportunities that are not readily available through their academic programs, limiting their professional development.",
            "pitch": "Gain valuable mentorship and internship opportunities through Sundai Club's partnerships with local businesses, helping you build a strong foundation for your career."
        },
        {
            "hypothesis": "The club's commitment to inclusivity can play a vital role in diversifying the tech and entrepreneurial landscape, addressing societal challenges related to representation and equity in these fields.",
            "pain_point": "The tech and entrepreneurship sectors often lack diversity, which can stifle innovation and limit the range of perspectives that drive progress.",
            "pitch": "Join Sundai Club to be part of an inclusive community that champions diverse perspectives in technology and entrepreneurship, paving the way for a more equitable future."
        }
    ]

    # Call the synchronous function
    results = process_multiple_jsons(json_list)

    # Print the results with context
    for context, result in results:
        print(f"{context}: {result}")
