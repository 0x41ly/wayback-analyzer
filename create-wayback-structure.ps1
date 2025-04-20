$basePath = "."

# Folder structure
$folders = @(
    "$basePath",
    "$basePath\wayback_tool",
    "$basePath\web",
    "$basePath\web\templates",
    "$basePath\web\static",
    "$basePath\output",
    "$basePath\wayback_tool\db"
)

# File structure
$files = @(
    "$basePath\main.py",
    "$basePath\requirements.txt",
    "$basePath\README.md",
    "$basePath\setup.py",
    "$basePath\wayback_tool\__init__.py",
    "$basePath\wayback_tool\cli.py",
    "$basePath\wayback_tool\fetcher.py",
    "$basePath\wayback_tool\parser.py",
    "$basePath\wayback_tool\analyzer.py",
    "$basePath\wayback_tool\utils.py",
    "$basePath\wayback_tool\writer.py",
    "$basePath\wayback_tool\db.py",           # 🔥 MongoDB integration
    "$basePath\web\app.py",
    "$basePath\web\routes.py"
    "$basePath\wayback_tool\db\__init__.py",          # Initializes db module
    "$basePath\wayback_tool\db\db_handler.py",        # MongoDB connection logic
    "$basePath\wayback_tool\db\models.py",            # Pydantic models (Endpoint, Param, Response)
    "$basePath\wayback_tool\db\db_operations.py",     # Handles DB operations (save, update, delete)
    "$basePath\wayback_tool\db\db.py"   
)

# Create folders
foreach ($folder in $folders) {
    if (-Not (Test-Path $folder)) {
        New-Item -Path $folder -ItemType Directory | Out-Null
    }
}

# Create files
foreach ($file in $files) {
    if (-Not (Test-Path $file)) {
        New-Item -Path $file -ItemType File | Out-Null
    }
}

Write-Host "✅ Project structure with MongoDB support created at: $basePath"


