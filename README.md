# Protein-Design-and-Drug-Discovery-Research-Assistant

Overview
The Protein Design Research Assistant is a comprehensive web application that leverages NVIDIA's Inference Microservices (NIMs) and LlamaIndex for advanced protein design and analysis. This application is specifically designed to run in Google Colab, providing easy access to GPU resources and avoiding local dependency conflicts.

🎯 Purpose
This project was developed for the LlamaIndex-NVIDIA Developer Contest to demonstrate the effective integration of NVIDIA's AI services with LlamaIndex for protein design applications. The application showcases how to:
Utilize NVIDIA's Inference Microservices (NIMs) for protein structure prediction and design
Implement LlamaIndex for efficient knowledge retrieval and context-aware responses
Leverage Google Colab's GPU resources for optimal performance

🚀 Features

Literature Search: Search and analyze scientific papers from arXiv and PubMed
AI-generated paper summaries
Voice-enabled chat assistance
Integration with NVIDIA knowledge base

PDB Tools
Abstract lookup for quick protein information
PDB file download capabilities
Interactive 3D structure visualization
AI-powered structure analysis

RFdiffusion
Generate new protein structures
GPU-accelerated protein backbone generation
Custom binder design capabilities
Parameter optimization with AI assistance

ProteinMPNN
Optimize amino acid sequences
Deep learning-based sequence prediction
Integration with NVIDIA GPU acceleration
Advanced parameter configuration

AlphaFold2
Protein structure prediction
NVIDIA NGC optimization
Parameter customization
Results analysis and visualization

MolMIM
Molecular generation and optimization
CMA-ES algorithm implementation
Latent space exploration
Property optimization

DiffDock
Molecular docking via diffusion models
Score-based pose generation
Confidence model ranking
GPU-accelerated calculations

GROMACS
Molecular dynamics simulation protocols
NVIDIA GPU optimization
DeepSeek-enhanced protocol generation
Performance analysis

📋 Prerequisites

API Keys Required

NVIDIA API Key (Required)
Sign up at NVIDIA Developer Portal
Generate API key for accessing NIMs

https://build.nvidia.com/deepseek-ai/deepseek-coder-6_7b-instruct


OpenAI API Key (Required)
For GPT-4 integration and voice synthesis

https://platform.openai.com/docs/overview


Pinecone API Key (Required)
For vector database functionality

https://www.pinecone.io/


Phoenix API Key (Required)
For enhanced monitoring and tracing

https://phoenix.arize.com/


Google Colab Requirements
A Google account
Access to Google Colab
Sufficient Colab credits for GPU usage

https://colab.research.google.com/


🛠️ Installation

Open the Google Colab notebook 
Run the initial setup cell to install dependencies:

python

!pip install -r requirements.txt

Configure your environment variables:

import os
os.environ["NVIDIA_API_KEY"] = "your_key_here"
os.environ["OPENAI_API_KEY"] = "your_key_here"
os.environ["PINECONE_API_KEY"] = "your_key_here"
os.environ["PHOENIX_API_KEY"] = "your_key_here"  

💻 Usage
Starting the Application
Run all cells in the Colab notebook
Click the generated Gradio link to access the web interface
Navigate through different tabs for specific functionalities
Example Workflows

Protein Structure Generation
# Example using RFdiffusion
1. Upload PDB file
2. Set contig string
3. Specify hotspot residues
4. Adjust diffusion steps
5. Generate and run script

Sequence Optimization
# Example using ProteinMPNN
1. Upload structure
2. Configure parameters
3. Generate sequences
4. Analyze results
🔍 Technical Details

Architecture
Frontend: Gradio web interface
Backend: Python with multiple AI services
Database: Pinecone vector store
AI Models: NVIDIA NIMs integration
Monitoring: Phoenix telemetry

Key Components
LlamaIndex for knowledge retrieval
OpenAI GPT-4o for chat assistance
NVIDIA NIMs for protein design
OpenTelemetry for monitoring

⚠️ Important Notes
This application is specifically designed for Google Colab to avoid dependency conflicts and leverage cloud GPU resources
Local installation is not recommended due to complex dependencies
Some features may require specific GPU resources in Colab
API usage may incur costs depending on your service plans

🐛 Known Issues
Dependency conflicts when running locally
Specific CUDA version requirements
Memory limitations in free Colab tier
Timeout issues with long-running processes

📚 Resources
NVIDIA NIMs Documentation
LlamaIndex Documentation
Google Colab Documentation
Gradio Documentation

🤝 Contributing
This project is currently part of the LlamaIndex-NVIDIA Developer Contest and is not accepting external contributions.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

👥 Authors
Joseph Steward - Initial work - GitHub

🙏 Acknowledgments
NVIDIA for providing NIMs and GPU resources
LlamaIndex team for vector store capabilities
Google Colab for cloud computing resources
OpenAI for language model support

📧 Contact
For questions and support, please contact jsteward2930@gmail.com

Note: This project is a submission for the LlamaIndex-NVIDIA Developer Contest and is optimized for Google Colab usage. Local installation is not supported.

