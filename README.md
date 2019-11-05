<h1>5602-Mozilla</h1>
Ahmed Al Hasani, Alex Costinescu, and Pratik Revankar

<h2>Information about our Visualizations</h2>

<h3>Privacy & Tech  Awareness Score Across the Globe</h3>
<p>The geographical visualization shows a score of the tech knowledge and privacy priorities each country averaged. The visualization shows this by utilizing color to reflect each country’s score in the world map. The darker the color the higher the score, and vice versa.</p>

<h3></h3>
<p></p>

<h3></h3>
<p></p>

<h2>Design Process</h2>

<h3>Privacy & Tech  Awareness Score Across the Globe</h3>
<p>When we read the problem statement by Mozilla, and looked at the survey with the results, we started asking ourselves what questions interest us about the problem and the results. What are trends that we want to uncover, find out, and share with everyone. We wanted to find correlations between different traits across countries. We wanted to find out how tech savvy or tech aware respondents are and how this positively/negatively correlate with how important privacy is deemed and whom they trust. Does a person trust less and views privacy more important the more knowledge he/she is about technology? Are there outliers to the general trend we will uncover?</p>
<p>Our geographical visualization resulted from the question: does privacy priorities and tech awareness correlate and vary across different countries?</p>
<p>As a result, it was evident a geographical visualization would be constructed. As all of us are comfortable with programming, and Python was a common programming language we were familiar with, we opted to create our visualizations with various Python packages. </p>
<p>Python’s Plotly provides easy to use functions to create map objects that would combine seamlessly with Pandas’s dataframes which is what we used to store the dataset and preprocess it for Plotly’s geographical objects functionality. Additionally, Plotly outputs a single HTML file independent of the dataset and the packages required to create the visualization, which was very convenient for this project.</p>
<p>Plotly’s chropleth graph/map will allow us to communicate position, and the color functionality provided by Plotly will allow us to communicate a second dimension, which in our is the score. We believed that the default color scale provided by the choropleth function was appropriate versus the red/blue color scale, because the default one was able to capture the different scores nearby and faraway countries accurately, rather than shades of blue or red which we believed made it harder to understand how one location varied exactly with another location.  </p>
<p>To keep the visualization simple and clean, we wanted to capture two main attributes (privacy priorities and tech awareness) through one measure. As a result, we decided we will multiply the two scores, and the color scale will reflect this overall score. We opted to follow this approach, rather than have two color scales, or two different visualization channels to communicate the two different attributes.</p>
<p>Additionally, this allowed us to capture and communicate outliers in an interesting way. Is there a country with a high/low score even when the privacy and tech awareness scores were different in magnitude (where one score was significantly higher than the other)? This is further discussed under the tasks section.</p>
<p>As a result, this visualization includes mostly quantitative data.</p>

<h2>Preprocessing Steps</h2>

<h3>Privacy & Tech  Awareness Score Across the Globe</h3>
<p>The preprocessing steps completed for this visualization included:</p>
<ol>
  <li>Create a subset of the dataset. The subset includes the columns listed below. The first two columns are privacy priorities and fear columns, the rest of the columns (except for countries) will reflect a respondent’s tech awareness (what devices they have and what topics they can explain).<br /><br />
    <span style="font-size:0.875em">
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
    </span>
    <br />
  </li>
  <li>Then, all the columns are converted into dummy columns using pandas’ function get_dummies. The first column is already numerical, but the rest of the columns basically contain an answer or an NaN value, hence, for a particular data row, if the user answered that question, the cell will be converted to 1, otherwise, 0. Additionally, if the user answered that their biggest fear was privacy, the user would receive 1, otherwise, 0. The first column however asks the user for the features they deem important (by ranking them) when they buy a new product. If privacy scored 10, then it means its not important, but if it received 1, the user pyritizes privacy. To capture this, the order of privacy would be subtracted by 11 and multiplied by -1, hence, an answer of ‘1’ would actually be 10 (10 being very important, where 1 would then mean not as important compared to other features).</li>
  <li>We summed up all the scores 1’s for the tech awareness topics and privacy related topics as well. We averaged the scores for each country. </li>
  <li>We added one more column, which is the country code for each country. Plotly requires a country_code column. Hence, Fiji would be FIJ, and Canada would be CAN. This was done using the package pycountry.</li>
  <li>Finally, the last column is the total score, which is the average privacy score (the higher the score, the more important privacy is to respondents in that country) multiplied by the tech awareness score.</li>
  <li>The final dataframe will then be passed to the choropleth function from plotly geographical_objects module. </li>
</ol>

<h2>Interactivity</h2>

<h3>Privacy & Tech  Awareness Score Across the Globe</h3>
<p>This visualization provides interactivity through a hover tool. If the user hovers over a specific country, the data for that specific country will be shown, which includes score, name of country, privacy score, tech awareness score, and the total score. </p>

<h2>Tasks Accomplished</h2>

<p>Our questions resulted from our curiosity and the desire to create entertaining and interactive visualizations that enable us and users to learn about the survey’s results in a quick and lighthearted manner. Below are lists of tasks each visualization accomplishes:</p>

<h3>Privacy & Tech  Awareness Score Across the Globe</h3>
<p>As mentioned earlier, we wanted to create a geographical visualization to communicate information in a quick, straightforward, and entertaining manner. We also believed the visualization will introduce a fun way of picking out outliers. Are there light-colored countries in a sea of dark colored countries, or vice versa? If so, why? What are their traits? Do these countries exhibit different traits (more tech aware, more concerned about privacy)? For instance, Russia has a dark color, because they have a high tech awareness score, but a lower privacy priority score as opposed to countries like the UK and Australia, which overall high a high (not as high as Russia’s) tech awareness score and a high privacy priority concern (less than Russia’s privacy concern score).</p>
<p>As a result, we focused on these tasks for this visualization:</p>
<ul>
  <li>Present: exhibit data from the survey’s findings and our simple analysis in a visual manner through color and positioning. </li>
  <li>Search: lookup a specific country and its results or find the highest scored countries (countries that are highly tech aware or deem privacy more important than other countries), or locate a specific country to find its traits. </li>
  <li>Query: compare two countries, two continents with each other to uncover general trends simply by hovering over them to view their respective results. Summarize the overall trends and correlation which is communicated by the color variation in different locations.</li>
  <li>Outlier detection: there are countries in the middle of a ‘yellow sea’ that are darker in color, why are these countries different than their neighbors? </li>
</ul>

<h2>Data Attributes</h2>

<h3>Privacy & Tech  Awareness Score Across the Globe</h3>
<ul>
  <li>Country</li>
  <li>Privacy Score</li>
  <li>Tech Awareness Score</li>
</ul>

<h2>How to Run</h2>

<h2>Team Member Roles</h2>

<ul>
  <li><strong>Ahmed:</strong> Created the <em>Privacy & Tech  Awareness Score Across the Globe</em> visualization.</li>
</ul>
