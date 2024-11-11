# ProteinMPNN API Script
import requests
import os
import json
from pathlib import Path

def get_api_key():
    """Get the Nvidia API key from environment variable or user input."""
    return os.getenv("NVCF_RUN_KEY") or input("Paste your Nvidia API Key: ")

def get_pdb_structure(pdb_id):
    """Download a PDB structure file."""
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to download PDB structure: {pdb_id}")

def run_proteinmpnn(api_key, input_pdb, **kwargs):
    """Run ProteinMPNN prediction using the Nvidia API."""
    url = "https://health.api.nvidia.com/v1/biology/ipd/proteinmpnn/predict"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    payload = {
        "input_pdb": input_pdb,
        "ca_only": kwargs.get("ca_only", False),
        "use_soluble_model": kwargs.get("use_soluble_model", False),
        "random_seed": kwargs.get("random_seed", 0),
        "num_seq_per_target": kwargs.get("num_seq_per_target", 1),
        "sampling_temp": kwargs.get("sampling_temp", [0.1]),
        # Add more parameters as needed
    }
    
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    return response

def save_output(response, output_file="output.fa"):
    """Save the ProteinMPNN output to a file."""
    Path(output_file).write_text(json.loads(response.text)["mfasta"])
    print(f"Output saved to {output_file}")

def main():
    try:
        # Get the Nvidia API key
        api_key = get_api_key()
        
        # Get the PDB structure (replace with your desired PDB ID)
        pdb_id = "1R42"
        input_pdb = get_pdb_structure(pdb_id)
        
        # Run ProteinMPNN
        response = run_proteinmpnn(api_key, input_pdb)
        
        save_output(response)
    except requests.RequestException as e:
        print(f"Network error: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing API response: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()