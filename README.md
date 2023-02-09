<h1>Bitcoin Address Transaction Finder</h1>

<p>This script prompts the user to input one or more Bitcoin addresses, and then finds all transactions involving each address.</p>

<h2>Getting Started</h2>

<p>To run this script, you will need Python 3 installed on your computer.</p>

<ol>
  <li>Clone the repository:</li>
</ol>

<pre>
<code>git clone https://github.com/your-username/bitcoin-address-transaction-finder.git</code>
</pre>

<ol start="2">
  <li>Navigate to the repository directory:</li>
</ol>

<pre>
<code>cd bitcoin-address-transaction-finder</code>
</pre>

<ol start="3">
  <li>Run the script:</li>
</ol>

<pre>
<code>python3 main.py</code>
</pre>

<h2>How it Works</h2>

<p>The script prompts the user to enter a Bitcoin address. The user can enter as many addresses as they like, and can stop by entering "done".</p>

<p>For each address, the script calls the `find_transactions` function, which should be implemented to find all transactions involving that address and return a list of dictionaries, each representing a transaction.</p>

<p>The script then prints the number of transactions involving each address, as well as the other address involved in each transaction and the amount transferred.</p>

<h2>Contributions</h2>

<p>Feel free to contribute to this project by adding new features, fixing bugs, or improving the documentation. Just fork the repository, make your changes, and submit a pull request.</p>
