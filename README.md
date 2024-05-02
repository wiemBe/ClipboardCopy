# ClipboardCopy

ClipboardCopy is a Python script that copies the clipboard contents and sends them to another IP address. It can be useful for scenarios where you need to share clipboard data across different machines or devices.

## Required Frameworks

Before running the script, make sure you have the following frameworks installed:

- **pywin32**: Used for accessing the clipboard on Windows. `pip install pywin32`

- **schedule**: Used for scheduling tasks to run at specific intervals. `pip install schedule`

## Usage

1. Install the required frameworks using the provided pip commands.

2. Run the `main.py` script.

3. Specify the IP address of the destination where you want to send the clipboard contents.

4. The script will continuously monitor the clipboard and send its contents to the specified IP address at regular intervals.

## Example

```bash
# Example usage
python3 main.py
