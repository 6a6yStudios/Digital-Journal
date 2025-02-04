<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Journal - README</title>
    <style>
        body {
            font-family: 'Courier New', Courier, monospace;
            background-color: #121212;
            color: #e5e5e5;
            margin: 0;
            padding: 0;
            overflow-x: hidden;
        }

        header {
            background-color: #1f1f1f;
            padding: 20px 0;
            text-align: center;
            border-bottom: 2px solid #333;
        }

        header h1 {
            color: #ff61a6;
            font-size: 3em;
            letter-spacing: 2px;
        }

        h2 {
            color: #79e2f1;
            font-size: 1.5em;
            margin-top: 20px;
        }

        p, ul, ol {
            line-height: 1.8;
        }

        pre, code {
            background-color: #2a2a2a;
            border-radius: 5px;
            color: #e0e0e0;
            font-family: 'Courier New', Courier, monospace;
            padding: 10px;
            border: 1px solid #444;
            overflow-x: auto;
        }

        pre {
            padding: 15px;
            margin: 15px 0;
        }

        ul, ol {
            list-style: none;
            padding-left: 0;
        }

        ul li, ol li {
            padding-left: 20px;
            position: relative;
        }

        ul li::before, ol li::before {
            content: '►';
            position: absolute;
            left: 0;
            color: #79e2f1;
        }

        .section {
            margin: 30px;
        }

        footer {
            background-color: #1f1f1f;
            color: #757575;
            text-align: center;
            padding: 20px 0;
            font-size: 0.9em;
        }

        footer a {
            color: #ff61a6;
            text-decoration: none;
        }

        footer a:hover {
            text-decoration: underline;
        }

        .highlight {
            background-color: #333;
            border-radius: 5px;
            padding: 5px;
            color: #ff61a6;
        }

    </style>
</head>
<body>

    <header>
        <h1>Digital Journal</h1>
    </header>

    <div class="section">
        <h2>Project Overview</h2>
        <p>A simple, customizable digital journal built in Python. Allows users to:</p>
        <ul>
            <li>Add journal entries with dates</li>
            <li>View all journal entries</li>
            <li>Search entries by date</li>
        </ul>
    </div>

    <div class="section">
        <h2>Features</h2>
        <ul>
            <li>Easy-to-use command-line interface (CLI)</li>
            <li>Save entries in a text file</li>
            <li>Search and view past entries by date</li>
        </ul>
    </div>

    <div class="section">
        <h2>Usage</h2>
        <p>1. Clone or download the repository.</p>
        <p>2. Make sure you have Python 3.x installed.</p>
        <p>3. Run <span class="highlight">journal.py</span> using the command:</p>
        <pre><code>python journal.py</code></pre>
        <p>4. Choose an option from the menu:</p>
        <ul>
            <li><strong>Add Entry</strong>: Add a new journal entry.</li>
            <li><strong>View Entries</strong>: View all saved journal entries.</li>
            <li><strong>Search Entries by Date</strong>: Search for entries on a specific date.</li>
            <li><strong>Exit</strong>: Exit the program.</li>
        </ul>
    </div>

    <div class="section">
        <h2>Contributing</h2>
        <p>Feel free to fork the repository, improve it, and submit pull requests. Contributions are always welcome!</p>
    </div>

    <div class="section">
        <h2>License</h2>
        <p>This project is open-source and available under the MIT License.</p>
    </div>

    <footer>
        <p>Made with ❤️ by <a href="https://github.com/6a6yStudios" target="_blank">6a6y Studios LLC</a></p>
    </footer>

</body>
</html>
