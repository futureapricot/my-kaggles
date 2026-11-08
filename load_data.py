from pathlib import Path

import kagglehub

# Downloads the dataset CSV files into a folder here
kagglehub.dataset_download(
    "psparks/instacart-market-basket-analysis",
    output_dir=str(Path(__file__).parent / "instacart-market-basket-analysis"),
)
