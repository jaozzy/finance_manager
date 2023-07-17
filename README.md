<strong><h1>Guia de Uso (English Version Bellow):</h1></strong>

<strong><h2>Instalando códigos e dados necessários:</h2></strong>

<h3>Clone o repositório digitando esse comando em seu terminal (Certifique-se de ter instalado o git em seu dispositivo)</h3>

<pre>
<code>git clone https://github.com/jaozzy/finance_manager</code>
</pre>

<h3>Instale as dependências:</h3>

<p>No diretório do repositório, abra um terminal e digite esse comando (Certifique-se de ter python instalado em seu dispositivo):</p>

<pre>
<code>pip install -r requirements.txt</code>
</pre>

<strong><h2>Inserindo Informações no Sistema:</h2></strong>

<p>Insira as informações no sistema através do arquivo "info_insert.py", seguindo a seguinte formatação:</p>
<p>data, tipo, categoria, método, valor</p>

<strong><h3>Exemplo:</h3></strong>

<pre>
<code>10/01/2023, r, salário, pix, 3250.00,</code>
</pre>

<h3>Formatação:</h3>

<p>&lt;data&gt; Deve seguir a formatação "dd/mm/aaaa"</p>
<p>&lt;tipo&gt; Deve ser somente "r" ou "d" minúsculo. "r" representa RECEITA e "d" representa DESPESA</p>
<p>&lt;categoria&gt; Deve ter somente uma palavra, representando a CATEGORIA da despesa ou da receita. ex: ALIMENTAÇÃO</p>
<p>&lt;método&gt; Deve ter somente uma palavra, representando o MÉTODO DE PAGAMENTO da despesa ou da receita. ex: DINHEIRO</p>
<p>&lt;valor&gt; Deve ser um valor numérico apresentando duas casas após a vírgula (a vírgula deve ser substituída por um "."). ex: 25.90 (25 reais e 90 centavos)</p>

<h3>OBS:</h3>
<p>Sempre escreva uma vírgula entre os dados e no final da linha (da última também)!</p>

<strong><h3>Exemplo de como os dados devem ser inscritos:</h3></strong>

![Imagem 1](https://github.com/jaozzy/finance_manager/blob/master/img/database_example.png)

<strong><h2>Executando a Análise dos Dados:</h2></strong>

<p>Execute o arquivo "main.py" e pronto! O arquivo Excel, os gráficos e o relatório foram criados! No final, você só precisa digitar o email que vai receber o relatório.</p>

<p><h2>Exemplo de gráfico:</h2></p>

![Imagem 2](https://github.com/jaozzy/finance_manager/blob/master/graphs/grafico_despesas_categoria.png)

<strong><h3>Qualquer dúvida ou problema no código, entre em contato comigo via whatsapp ou email. (ambos no perfil do GitHub)</h3></strong>

<hr>

<strong><h1>User Guide:</h1></strong>

<strong><h2>Installing necessary code and data:</h2></strong>

<h3>Clone the repository by typing this command in your terminal (Make sure you have Git installed on your device):</h3>

<pre>
<code>git clone https://github.com/jaozzy/finance_manager</code>
</pre>

<h3>Install the dependencies:</h3>

<p>In the repository directory, open a terminal and type this command (Make sure you have Python installed on your device):</p>

<pre>
<code>pip install -r requirements.txt</code>
</pre>

<strong><h2>Entering Information in the System:</h2></strong>


<p>Enter the information into the system through the "info_insert.py" file, following the following format:</p>
<p>date, type, category, method, value</p>

<strong><h3>Example:</h3></strong>

<pre>
<code>01/10/2023, r, salary, pix, 3250.00,</code>
</pre>

<h3>Formatting:</h3>
<p>&lt;date&gt; should follow the format "dd/mm/yyyy"</p>
<p>&lt;type&gt; should be either "r" or "d" in lowercase. "r" represents REVENUE and "d" represents EXPENSE</p>
<p>&lt;category&gt; should have only one word, representing the CATEGORY of the expense or revenue. e.g., FOOD</p>
<p>&lt;method&gt; should have only one word, representing the PAYMENT METHOD of the expense or revenue. e.g., CASH</p>
<p>&lt;value&gt; should be a numeric value with two decimal places (use a "." instead of a comma). e.g., 25.90 (25 dollars and 90 cents)</p>
<h3>NOTE:</h3>

<p>Always write a comma between the data and at the end of the line (including the last line)!</p>

<strong><h3>Example of how the data should be entered:</h3></strong>

![Image 1](https://github.com/jaozzy/finance_manager/blob/master/img/database_example.png)

<strong><h2>Running Data Analysis:</h2></strong>

<p>Run the "main.py" file and you're done! The Excel file, graphs, and report have been created! In the end, you just need to enter the email that will receive the report.</p>

<p><h2>Example of a graph:</h2></p>

![Image 2](https://github.com/jaozzy/finance_manager/blob/master/graphs/grafico_despesas_categoria.png)

<strong><h3>If you have any questions or issues with the code, please contact me via WhatsApp or email. (both on the GitHub profile)</h3></strong>
