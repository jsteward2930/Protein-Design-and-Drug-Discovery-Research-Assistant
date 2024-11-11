import requests
import os
import json
from pathlib import Path

def sequence_to_pdb(sequence):
    # Convert a sequence of amino acids to a simple PDB format
    pdb_lines = []
    for i, aa in enumerate(sequence, start=1):
        x, y, z = i * 3.8, 0, 0  # Simple linear placement of CA atoms
        pdb_lines.append(f"ATOM  {i:5d}  CA  {aa:3} A{i:4d}    {x:8.3f}{y:8.3f}{z:8.3f}  1.00  0.00           C")
    return "\n".join(pdb_lines)

def run_proteinmpnn(input_sequence, ca_only, use_soluble_model, random_seed, num_seq_per_target, sampling_temp, api_key):
    # Use the provided API key
    key = api_key or os.getenv("NVCF_RUN_KEY")
    if not key:
        raise ValueError("API key is not provided and NVCF_RUN_KEY environment variable is not set")

    # Convert input sequence to PDB format
    pdb_content = sequence_to_pdb(input_sequence.upper())

    # Prepare the request payload
    payload = {
        "input_pdb": pdb_content,
        "ca_only": True,
        "use_soluble_model": False,
        "sampling_temp": 0.1,
        "num_seq_per_target": 1
    }

    # Add random_seed to payload if provided
    payload["random_seed"] = 1

    # Make the API request
    response = requests.post(
        url=os.getenv("URL", "https://health.api.nvidia.com/v1/biology/ipd/proteinmpnn/predict"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}"
        },
        json=payload,
        timeout=30
    )
    
    # Check for successful response
    response.raise_for_status()
    
    # Parse and return the result
    result = response.json()
    return result["mfasta"]

# Run the ProteinMPNN prediction
input_sequence = "LEEKKVCQGTSNKLTQLGTFEDHFLSLQRMFNNCEVVLGNLEITYVQRNYDLSFLKTIQEVAGYVLIALNTVERIPLENLQIIRGNMYYENSYALAVLSNYDANKTGLKELPMRNLQEILHGAVRFSNNPALCNVESIQWRDIVSSDFLSNMSMDFQNHLGSCQKCDPSCPNGSCWGAGEENCQKLTKIICAQQCSGRCRGKSPSDCCHNQCAAGCTGPRESDCLVCRKFRDEATCKDTCPPLMLYNPTTYQMDVNPEGKYSFGATCVKKCPRNYVVTDHGSCVRACGADSYEMEEDGVRKCKKCEGPCRKVCNGIGIGEFKDSLSINATNIKHFKNCTSISGDLHILPVAFRGDSFTHTPPLDPQELDILKTVKEITGFLLIQAWPENRTDLHAFENLEIIRGRTKQHGQFSLAVVSLNITSLGLRSLKEISDGDVIISGNKNLCYANTINWKKLFGTSGQKTKIISNRGENSCKATGQVCHALCSPEGCWGPEPRDCVSHHHHHH"
api_key = "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"  # The API key provided by the user
result = run_proteinmpnn(input_sequence, True, False, 1, 1, 0.1, api_key)

print("ProteinMPNN Result:")
print(result)

# Save the result to a file
output_file = Path("proteinmpnn_output.fa")
output_file.write_text(result)
print(f"Result saved to {output_file}")