#!/usr/bin/env python3
import os
import requests
import time
from pathlib import Path

# Variables
key = os.getenv("NVCF_RUN_KEY") or input("Paste the Run Key: ")
url = os.getenv("URL", "https://health.api.nvidia.com/v1/biology/deepmind/alphafold2-multimer")
status_url = os.getenv("STATUS_URL", "https://health.api.nvidia.com/v1/status")

sequences = [
    "AAAAEDAARWATFIANYEELKAGTWAALERVAAAGPEGAACGLADWLAEREGPTPELAAIRALRTAEALRAHLAAVMAEFDAALAVAGLPLSAYIRGMAAMSGFDPDYEEALPDGRTRVGLFGILT",
    "AAAAEDAARWATFIANYEELKAGTWAALERVAAAGPEGAACGLADWLAEREGPTPELAAIRALRTAEALRAHLAAVMAEFDAALAVAGLPLSAYIRGMAAMSGFDPDYEEALPDGRTRVGLFGILT"
]

output_file = Path("output.json")

# Request to predict structure from a list of sequences
headers = {
    "content-type": "application/json",
    "Authorization": f"Bearer {key}",
    "NVCF-POLL-SECONDS": "5",
}

data = {
    "sequences": sequences,
    "algorithm": "jackhmmer",
    "e_value": 0.0001,
    "iterations": 1,
    "databases": ["uniref90", "small_bfd", "mgnify"],
    "relax_prediction": True,
    "structure_models_to_relax": "all",
    "num_predictions_per_model": 1,
    "max_msa_sequences": 512,  # Adjusted to a typical default value
    "template_searcher": "hhsearch"
}

print("Making request...")
response = requests.post(url, headers=headers, json=data)

# Check the status code
if response.status_code == 200:
    output_file.write_text(response.text)
    print(f"Response output to file: {output_file}")
elif response.status_code == 202:
    print("Request accepted...")
    # Extract reqId header
    req_id = response.headers.get("nvcf-reqid")

    # Poll the /status endpoint
    while True:
        print("Polling for response...")
        status_response = requests.get(f"{status_url}/{req_id}", headers=headers)

        if status_response.status_code != 202:
            output_file.write_text(status_response.text)
            print(f"Response output to file: {output_file}")
            break

        # Wait before polling again
        time.sleep(5)
else:
    print(f"Unexpected HTTP status: {response.status_code}")
    print(f"Response: {response.text}")
