# Commit For Free

A sophisticated Git commit message generator that uses AI to create meaningful, conventional commit messages based on your code changes.

## Features

- 🤖 AI-powered commit message generation using GPT models
- 📝 Follows [Conventional Commits](https://www.conventionalcommits.org/) format
- 🔍 Smart analysis of file changes and diffs
- 🎨 Beautiful CLI interface with rich formatting
- ⚡ Efficient handling of both small and large changes
- 🔄 Fallback mechanisms for reliability
- 🎯 Automatic change type detection (feat, fix, docs, etc.)
- 📊 Progress tracking and status display

## Installation

1. Clone the repository:
```bash
git clone https://github.com/alaamer12/c4f.git
cd c4f
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Simply run the script in your Git repository:

```bash
python c4f/cli.py [COMMANDS]
```

The tool will:
1. Detect staged and unstaged changes in your repository
2. Analyze the changes and their context
3. Generate an appropriate commit message using AI
4. Stage and commit the changes with the generated message

### Features in Detail

- **Smart Change Analysis**: Automatically detects the type of changes (feature, fix, documentation, etc.) based on file paths and content
- **Comprehensive Messages**: Generates detailed commit messages for larger changes with bullet points and breaking change notifications
- **Interactive Interface**: Displays changes in a formatted table and allows user interaction when needed
- **Progress Tracking**: Shows real-time progress for file analysis and commit operations
- **Fallback Mechanism**: Includes a fallback system if AI generation fails or times out

## Configuration

C4F can be configured through command-line arguments:

```bash
python c4f/cli.py [OPTIONS]
```

Available options:
- `-h, --help`: Show help message and exit
- `-v, --version`: Show program's version number and exit
- `-r, --root PATH`: Set the root directory [default: current project root]
- `-m, --model MODEL`: Set the AI model to use [default: gpt-4-mini]
- `-a, --attempts NUM`: Set the number of generation attempts [default: 3]
- `-t, --timeout SEC`: Set the fallback timeout in seconds [default: 10]
- `-f, --force-brackets`: Force conventional commit type with brackets [default: False]

Example usage:
```bash
python c4f/cli.py --model gpt-4 --attempts 5 --timeout 15
```

## Requirements

- Python 3.9+
- Git
- Required Python packages (see requirements.txt)
- Internet connection for AI model access

## Security

⚠️ **Important**: C4F is currently in its initial release (v0.1.0) and does not provide any security guarantees. Please read our [SECURITY.md](SECURITY.md) file for:
- Current security status
- Known limitations
- Future security plans
- How to report issues

## Code of Conduct

We want to foster an inclusive and welcoming environment. All participants in our project are expected to follow basic principles of respect and professionalism. While we don't have formal guidelines yet, please:

- Be respectful and inclusive
- Avoid offensive or harmful behavior
- Help others when possible
- Keep discussions constructive

## Contributing

We love contributions! The process is simple:

1. Fork the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Make your changes
4. Submit a Pull Request

That's it! No complex rules or constraints. Feel free to:
- Fix bugs
- Add features
- Improve documentation
- Suggest ideas

See our [ROADMAP.md](ROADMAP.md) for planned features you might want to help with.

## Model Compatibility 

While c4f has been primarily tested with `gpt-4-mini`, `gpt-4`, and `gpt-3.5-turbo`, the underlying g4f library supports many additional models. However, please note:

⚠️ **Warning**: Although most g4f-supported models may technically work with c4f, they have not been extensively tested and are not officially recommended. Using untested models may result in:
- Lower quality commit messages
- Slower performance
- Unexpected errors or timeouts

For the best experience, we recommend using one of the officially supported models specified in the command-line options.

## License

This project is licensed under the MIT License - see the [LICENSE file](LICENSE) for details.

## Acknowledgments

- Built with [g4f](https://github.com/xtekky/gpt4free) for AI generation
  - Special thanks to the g4f library maintainers for making powerful AI models accessible
  - g4f enables this tool to generate high-quality commit messages without API keys
- Uses [rich](https://github.com/Textualize/rich) for beautiful terminal formatting