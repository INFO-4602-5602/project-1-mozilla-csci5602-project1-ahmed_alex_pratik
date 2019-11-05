<h1>5602-Mozilla</h1>
Ahmed Al Hasani, Alex Costinescu, and Pratik Revankar

<br />
<br />
<h2>How to Run</h2>
<p>The links to each visualization can be found here: <a href="https://info-4602-5602.github.io/project-1-mozilla-csci5602-project1-ahmed_alex_pratik/" target="_blank">https://info-4602-5602.github.io/project-1-mozilla-csci5602-project1-ahmed_alex_pratik/</a></p>

<br />
<br />
<h2>Information about our Visualizations</h2>

<h3>Privacy & Tech  Awareness Score Across the Globe</h3>
<p>This visualization shows a score of the tech knowledge and privacy priorities each country averaged. It shows this by utilizing color to reflect each country’s score on the world map. The darker the color, the higher the score, and vice versa.</p>

<h3>Trust vs. Knowledge</h3>
<p>This visualization shows where people are more likely to place their trust based on the number of connected devices that they own and their level of tech-savviness. Darker colors show less familiarity with technology, while lighter colors show more familiarity with tech based on how users responded to the survey.</p>

<h3>Importance of Privacy, Security, and Safety vs. Number of Online Connected Devices Owned</h3>
<p>This visualization displays the Number of Connected Devices a user owns in relation to the importance that they place on Privacy, Security, and Safety. Points are plotted based on the average answers per-country and the size of a circle is scaled based on the average tech-saviness of people surveyed from that country.</p>

<br />
<br />
<h2>Design Process</h2>
<p>When we read the problem statement by Mozilla and looked at the survey with the results, we started asking ourselves what questions interest us about the problem and the results. What are trends that we want to uncover, find out, and share with everyone. We wanted to find correlations between different traits across countries. We wanted to find out how tech savvy or tech aware respondents are and how this positively/negatively correlate with how important privacy is deemed and whom they trust. Does a person trust less and views privacy more important the more knowledge he/she is about technology? Are there outliers to the general trend we will uncover?</p>

<h3>Privacy & Tech  Awareness Score Across the Globe</h3>
<p>This visualization resulted from the following question: Does privacy priorities and tech awareness correlate and vary across different countries?</p>
<p>As a result, it was evident a geographical visualization would be constructed. As all of us are comfortable with programming, and Python was a common programming language we were familiar with, we opted to create our visualizations with various Python packages. </p>
<p>Python’s Plotly provides easy to use functions to create map objects that would combine seamlessly with Pandas’s dataframes which is what we used to store the dataset and preprocess it for Plotly’s geographical objects functionality. Additionally, Plotly outputs a single HTML file independent of the dataset and the packages required to create the visualization, which was very convenient for this project.</p>
<p>Plotly’s chropleth graph/map will allow us to communicate position, and the color functionality provided by Plotly will allow us to communicate a second dimension, which is the score. We believed that the default color scale provided by the choropleth function was appropriate versus the red/blue color scale, because the default one was able to capture the different scores nearby and faraway countries accurately, rather than shades of blue or red which we believed made it harder to understand how one location varied exactly with another location.</p>
<p>To keep the visualization simple and clean, we wanted to capture two main attributes (privacy priorities and tech awareness) through one measure. As a result, we decided to multiply the two scores, and the color scale will reflect this overall score. We opted to follow this approach, rather than have two color scales or two different visualization channels, to communicate the two different attributes in an easily interpretable way.</p>
<p>Additionally, this allowed us to capture and communicate outliers in an interesting way. Is there a country with a high/low score even when the privacy and tech awareness scores were different in magnitude (where one score was significantly higher than the other)? This is further discussed under the tasks section.</p>

<h3>Trust vs. Knowledge</h3>
<p>We wanted to explore the correlation between “trust” and “knowledge” of the respondents of the survey, to see <strong>whom they trust</strong> to educate them about online safety, security and privacy and their <strong>technology literacy</strong>, based on the number of terms they can explain. We also considered the number of online connected devices that they owned, to gain a sense of how dependent they are on technology and devices.</p>
<p>Since we were dealing with ‘categorical’ data attributes, we considered using a heat map, to plot data points, with each tile expressing the technology savviness score, for a particular ‘trustworthy entity’ and corresponding number of online devices they own.</p>
<p>We used an interactive visualization tool called Bokeh, since it allowed rapid development with Python. </p>

<h3>Importance of Privacy, Security, and Safety vs. Number of Online Connected Devices Owned</h3>
<p>We wanted to show a correlation between the number of online connected devices owned by respondents from around the world (grouped by country) , and how much importance they gave to safety, security and privacy before purchasing these technology products. We decided to use a scatter plot to visualize the distribution of the data across the countries, with each data point as a circle, whose radius was proportional to their technology savviness.</p>
<p>We used an interactive visualization tool called Bokeh, since it allowed rapid development with Python.</p>

<br />
<br />
<h2>Preprocessing Steps</h2>

<h3>Privacy & Tech  Awareness Score Across the Globe</h3>
<ol>
  <li>First, we created a subset of the data. This includes the columns listed below. The first two columns are privacy priorities and fear columns, while the rest of the columns (except for Countries) reflect a respondent’s tech awareness (what devices they have and what topics they can explain).<br /><br />
    <ul>
      <li>Privacy: You Are planning on buying your next cool new tech toy. Take a look at the items below and arrange them in order of importance as you make that purchase. (PRIVACY COLUMN)</li>
      <li>What is your biggest fear as we move towards a more connected future? (PRIVACY COLUMN)</li>
      <li>WiFi Router: Check all the internet connected devices you currently own</li>
      <li>Laptop computer: Check all the internet connected devices you currently own</li>
      <li>Smart phone: Check all the internet connected devices you currently own</li>
      <li>Smart TV: Check all the internet connected devices you currently own</li>
      <li>Activity Tracker (ex: Fitbit or Apple Watch): Check all the internet connected devices you currently own</li>
      <li>Smarthome Hub (ex. Amazon Echo, Google Alexa): Check all the internet connected devices you currently own</li>
      <li>Car that connects to the internet: Check all the internet connected devices you currently own</li>
      <li>Smart Thermostat (ex: Nest): Check all the internet connected devices you currently own</li>
      <li>Smart Appliance (ex. Coffeemaker, Refrigerator, Oven, Fridge): Check all the internet connected devices you currently own</li>
      <li>Smart Door Locks (ex. Door locks for your home you can open via bluetooth): Check all the internet connected devices you currently own</li>
      <li>Smart Lighting (ex. Connected lighting switches, dimmers, or bulbs): Check all the internet connected devices you currently own</li>
      <li>IoT: Check all the terms below that you could explain to a friend</li>
      <li>Connected Devices: Check all the terms below that you could explain to a friend</li>
      <li>Botnet: Check all the terms below that you could explain to a friend</li>
      <li>Blockchain: Check all the terms below that you could explain to a friend</li>
      <li>RFID: Check all the terms below that you could explain to a friend</li>
      <li>DDOS: Check all the terms below that you could explain to a friend</li>
      <li>Zero Day: Check all the terms below that you could explain to a friend</li>
      <li>VPN: Check all the terms below that you could explain to a friend</li>
      <li>TOR:Check all the terms below that you could explain to a friend</li>
      <li>Countries</li>
    </ul>
    <br />
  </li>
  <li>Then, we converted all of the columns into dummy columns using the Pandas function get_dummies. The first column is already numerical, but the rest of the columns basically contain an answer or an null value. Hence, for a particular data row, if the user answered that question, the cell is converted to 1, otherwise, 0. Additionally, if the user answered that their biggest fear was privacy, the user would receive 1, otherwise, 0. The first column however asks the user for the features they deem important (by ranking them) when they buy a new product. If privacy scored 10, then it means its not important, but if it received 1, the user pyritizes privacy. To capture this, the order of privacy would be subtracted by 11 and multiplied by -1, hence, an answer of ‘1’ would actually be 10 (10 being very important, where 1 would then mean not as important compared to other features).</li>
  <li>We summed up all the scores 1’s for the tech awareness topics and privacy related topics as well. We averaged the scores for each country. </li>
  <li>We added one more column, which is the country code for each country. Plotly requires a country_code column. Hence, Fiji would be FIJ, and Canada would be CAN. This was done using the package pycountry.</li>
  <li>Finally, the last column is the total score, which is the average privacy score (the higher the score, the more important privacy is to respondents in that country) multiplied by the tech awareness score.</li>
  <li>The final dataframe is then passed to the choropleth function from the plotly geographical_objects module. </li>
</ol>

<h3>Trust vs. Knowledge</h3>
<p>A subset of the data was created by first identifying the relevant columns, and then hot encoding the data fields so that we could work with numeric data for aggregation. We used Python DataFrames as input to the visualizations in Bokeh.</p>
<p>Columns for online connected devices and technology terms were encoded and aggregated, to get an overall score, for each respondent.</p>

<h3>Importance of Privacy, Security, and Safety vs. Number of Online Connected Devices Owned</h3>
<p>A subset of the data was created by first identifying the relevant columns, and then hot encoding the data fields so that we could work with numeric data for aggregation. 
We used Python DataFrames as input to the visualizations in Bokeh.</p>
<p>Columns for technology savviness, online connected devices and privacy, safety and security were encoded and aggregated, to get an overall score, for each respondent, by country.</p>

<br />
<br />
<h2>Interactivity</h2>

<h3>Privacy & Tech  Awareness Score Across the Globe</h3>
<p>This visualization provides interactivity through a hover tooltip. If the user hovers over a specific country, the data for that specific country is shown, which includes score, name of country, privacy score, tech awareness score, and the total score. </p>

<h3>Trust vs. Knowledge</h3>
<p>This visualization provides interactivity through a hover tooltip. If the user hovers over a specific tile, the data for that specific tile is shown, which includes Technology Literacy score, and the total number of responses.</p>

<h3>Importance of Privacy, Security, and Safety vs. Number of Online Connected Devices Owned</h3>
<p>This visualization provides interactivity through a hover tooltip. If the user hovers over a specific tile, the data for that specific tile is shown, which includes the country, number of responses, number of online connected devices, importance score of Privacy, Security and Safety, and Technology savviness score.</p>

<br />
<br />
<h2>Tasks Accomplished</h2>

<p>Our questions resulted from our curiosity and the desire to create entertaining and interactive visualizations that enable us and users to learn about the survey’s results in a quick and lighthearted manner. Below are lists of tasks each visualization accomplishes:</p>

<h3>Privacy & Tech  Awareness Score Across the Globe</h3>
<p>As mentioned earlier, we wanted to create a geographical visualization to communicate information in a quick, straightforward, and entertaining manner. We also believed the visualization should introduce a fun way of picking out outliers. Are there light-colored countries in a sea of dark colored countries, or vice versa? If so, why? What are their traits? Do these countries exhibit different traits (more tech aware, more concerned about privacy)? For instance, Russia has a dark color, because they have a high tech awareness score, but a lower privacy priority score as opposed to countries like the UK and Australia, which have high tech awareness AND privacy priority concern scores.</p>
<p>As a result, we focused on these tasks for this visualization:</p>
<ul>
  <li><strong>Present:</strong> Exhibit data from the survey’s findings and our simple analysis in a visual manner through color and positioning. </li>
  <li><strong>Search:</strong> Look up a specific country and its results or find the highest scored countries (countries that are highly tech aware or deem privacy more important than other countries), or locate a specific country to find its traits. </li>
  <li><strong>Query:</strong> Compare two countries, two continents with each other to uncover general trends simply by hovering over them to view their respective results. Summarize the overall trends and correlation which is communicated by the color variation in different locations.</li>
  <li><strong>Outlier Detection:</strong> There are countries in the middle of a ‘yellow sea’ that are darker in color, why are these countries different than their neighbors? </li>
</ul>

<h3>Trust vs. Knowledge</h3>
<p>We were able to analyze how technology literacy was correlated to the entity to trust based not he number of online connected devices that an individual owned.  We learnt that respondents who owned more devices were more technologically literate (could explain more technology terms), and had fairly equal distribution of whom to trust, with resources on online safety, security and privacy.</p>
<p>Respondents with highest literacy score, owned the max number of devices, and trusted Non-profit organizations like Mozilla and Consumer reports!</p>

<h3>Importance of Privacy, Security, and Safety vs. Number of Online Connected Devices Owned</h3>
<p>We were able to infer that people all over the world didn’t have the highest priority for Privacy, Security and Safety while purchasing the products, and own on average less than 5 connected devices. </p>
<p>The people in general also have an average tech. savviness score of ~ 3</p>

<br />
<br />
<h2>Data Attributes</h2>

<h3>Privacy & Tech  Awareness Score Across the Globe</h3>
<ul>
  <li>Country</li>
  <li>Privacy Score</li>
  <li>Tech Awareness Score</li>
</ul>

<h3>Trust vs. Knowledge</h3>
<ul>
  <li>Who do you most trust to help you learn how to protect your safety, security and privacy online.</li>
  <li>Number of terms they can explain</li>
  <li>Number of online connected devices they own</li>
</ul>

<h3>Importance of Privacy, Security, and Safety vs. Number of Online Connected Devices Owned</h3>
<ul>
  <li>I consider myself (tech savviness)</li>
  <li>Number of online connected devices they own</li>
  <li>Privacy, Security and Safety rankings</li>
</ul>

<br />
<br />
<h2>Team Member Roles</h2>

<ul>
  <li><strong>Ahmed:</strong> Created the <em>Privacy & Tech  Awareness Score Across the Globe</em> visualization.</li>
  <li><strong>Pratik:</strong> Created <em>Trust vs. Knowledge</em> and <em>Importance of Privacy, Security, and Safety vs. Number of Online Connected Devices Owned</em> visualizations.</li>
  <li><strong>Alex:</strong> Created <em>Trust vs. Knowledge</em> visualization and documentation/html pages.</li>
</ul>
