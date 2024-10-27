import streamlit as st
import pandas as pd
import plotly.express as px

# Title and introduction to the analysis
st.title("Wanna Get Hired? Let’s Uncover What’s Really Going On with Jobs in Saudi Arabia!")

st.write("""
Imagine this: you’re sitting at your computer, ready to kick off your job search. You log into **Jadarat**, wondering, “Where are the jobs? Who’s hiring? And what’s my salary going to look like?”

Don’t worry, I’ve got you covered. We’ve dived deep into Jadarat’s job data, and what we found? Well, it might just change how you approach your entire job hunt.

Trust me, there are a lot of surprises in here that you *need* to know.
""")

# Read the cleaned CSV file
Jadarat_df = pd.read_csv('cleaned_data.csv')

# --- Consistent Color Theme (Viridis) ---
color_theme = px.colors.sequential.Viridis

# --- First Question: Job Postings by Region ---
st.subheader("So, Let’s Talk Numbers – Where Are the Jobs?")
st.write("""
**Question #1:** If you could pick anywhere in Saudi Arabia to find a job, where would you go? Riyadh, Jeddah, Mecca?  
Guess what – the data is shouting **Riyadh** from the rooftops. **42.7%** of all job postings come from Riyadh alone! If you’re serious about landing a job, this is where you should be looking. Not far behind are **Mecca (25%)** and the **Eastern Province (14.7%)**.
""")

# Group by region and count job postings (Arabic column names)
region_job_count = Jadarat_df.groupby('المنطقة')['العنوان الوظيفي'].count().reset_index(name='عدد الوظائف')
region_job_count['النسبة'] = round((region_job_count['عدد الوظائف'] / region_job_count['عدد الوظائف'].sum()) * 100, 1)
region_job_count.sort_values(by='النسبة', ascending=False, inplace=True)

# Create a pie chart to visualize the proportion of job postings per region
fig1 = px.pie(
    region_job_count,
    values='النسبة',
    names='المنطقة',
    title="Proportion of Job Postings by Region",
    hole=0.3,   # Donut chart style
    width=700, 
    height=500,
    color_discrete_sequence=color_theme
)

# Embed the pie chart into the Streamlit app
st.plotly_chart(fig1)

st.write("""
But here's the kicker – if you’re looking outside these major cities, the job postings drop fast, with regions like Jazan and Hail offering under **3%** each. So, if you’re set on a specific region, be ready for a challenge!

*Tip for Job Seekers:* Head to Riyadh, Mecca, or the Eastern Province if you want to maximize your chances. The jobs are there, waiting for you.
""")

# --- Second Question: Gender Preferences ---
st.subheader("Gender Talk: Who’s Getting Hired More, Men or Women?")
st.write("""
**Question #2:** Does your gender play a role in how many job postings you’ll see? Let’s break this down.

Out of all the postings, **547** are wide open to *both* men and women, but here’s the twist: **458** are specifically looking for male candidates, while **399** are targeting female candidates.
""")

# Group by gender and count job postings (Arabic column names)
gender_job_counts = Jadarat_df.groupby('الجنس')['العنوان الوظيفي'].count().reset_index(name='عدد الوظائف')

# Create a bar chart to visualize job postings by gender
fig2 = px.bar(
    gender_job_counts,
    x='الجنس',  
    y='عدد الوظائف',  
    title="Job Postings by Gender",
    text='عدد الوظائف',  
    color_discrete_sequence=color_theme
)

# Customize the figure size and axis titles
fig2.update_layout(
    width=700, 
    height=500, 
    plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
    paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
    font=dict(color='grey'),  # Titles in grey
    xaxis_title='Gender',  
    yaxis_title='Number of Job Postings',
    xaxis=dict(showline=True, linewidth=1, linecolor='grey'),  # Grey axis lines
    yaxis=dict(showline=True, linewidth=1, linecolor='grey')   # Grey axis lines
)

# Show the bar chart in the Streamlit app
st.plotly_chart(fig2)

st.write("""
What does this tell us? There’s a growing trend toward gender-neutral postings, but the scales tip slightly in favor of men. So, if you’re a woman searching for a job, don’t feel discouraged – there are plenty of roles waiting for you, but knowing where to focus your efforts will make a huge difference.

*Key Insight for Employers:* This is the perfect time to implement more inclusive hiring practices, especially with the market leaning towards more balanced job roles.
""")

# --- Third Question: Fresh Graduates vs. Experienced Professionals ---
st.subheader("Fresh Graduate vs. Experienced: Who’s Winning the Job Game?")
st.write("""
**Question #3:** You might think that experience is the key to getting hired, right? Well, that’s not always the case here. The job market is actually super welcoming to fresh graduates right now.

Check this out – **826 job postings** are looking for fresh graduates, compared to **578** for experienced professionals. This means fresh talent is in demand more than ever, and companies are hungry for new perspectives.
""")

# Categorize job postings into 'Fresh Graduates' and 'Experienced'
Jadarat_df['Experience Category'] = Jadarat_df['سنوات الخبرة'].apply(lambda x: 'Fresh Graduates' if x == 0 else 'Experienced')

# Group by 'Experience Category'
job_postings_by_experience = Jadarat_df.groupby('Experience Category')['العنوان الوظيفي'].count().reset_index()

# Plot the distribution of job postings for fresh graduates and experienced
fig3 = px.bar(
    job_postings_by_experience,
    x='Experience Category',
    y='العنوان الوظيفي',
    title="Job Postings for Fresh Graduates vs Experienced Professionals",
    text='العنوان الوظيفي',
    color_discrete_sequence=color_theme
)

fig3.update_layout(
    width=700, 
    height=500, 
    plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
    paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
    font=dict(color='grey'),  # Titles in grey
    xaxis=dict(showline=True, linewidth=1, linecolor='grey'),  # Grey axis lines
    yaxis=dict(showline=True, linewidth=1, linecolor='grey')   # Grey axis lines
)

st.plotly_chart(fig3)

st.write("""
*Advice to Job Seekers:* If you’re fresh out of college, you’re in the driver’s seat. Companies are open to fresh talent, so don’t shy away from applying to roles you think you’d be great at. For experienced folks, this is your signal to stay sharp – employers still value your leadership and expertise.
""")

# --- Fourth Question: What Are the Most In-Demand Jobs? ---
st.subheader("The Big Question: What Are the Most In-Demand Jobs?")
st.write("""
**Question #4:** Let’s get to the heart of it – what roles are employers chasing after right now?

At the top of the list? **Drivers**, making up **26.9%** of the demand. Following close behind are **Sales representatives (20.5%)** and **Customer service specialists (9.52%)**.
""")

# Group by 'العنوان الوظيفي' and sum the 'الشواغر المتوفرة'
job_demand = Jadarat_df.groupby('العنوان الوظيفي')['الشواغر المتوفرة'].sum().reset_index()

# Select the top 10 jobs with the highest demand
top_jobs = job_demand.sort_values(by='الشواغر المتوفرة', ascending=False).head(10)

# Create a pie chart
fig4 = px.pie(
    top_jobs,
    values='الشواغر المتوفرة',
    names='العنوان الوظيفي',
    title="Top 10 Most In-Demand Jobs in Saudi Arabia",
    labels={'العنوان الوظيفي': 'Job Title', 'الشواغر المتوفرة': 'Available Vacancies'},
    hole=0.3,  # Donut chart style
    color_discrete_sequence=color_theme
)

# Customize layout
fig4.update_layout(
    width=800,
    height=500,
    paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
    font=dict(color='grey'),  # Titles in grey
    legend_title_text="Job Title"
)

st.plotly_chart(fig4)

st.write("""
It’s no surprise given Saudi Arabia’s retail and service boom – think of Vision 2030’s push to diversify the economy. Businesses need people who can engage with customers and drive sales, and they need them now.

*Pro Tip for Job Seekers:* If you’ve got experience in sales, driving, or customer service, polish that CV and get ready to shine. The demand is there, and now’s the time to act.
""")

# --- Fifth Question: Salary Expectations for Fresh Graduates ---
st.subheader("Now, Let’s Talk Money – What Can You Expect to Get Paid?")
st.write("""
Alright, now we get to the part everyone’s curious about: the paycheck. Whether you're just starting out or building up your experience, it’s good to know what you're worth.
""")

# Median Salary by Experience Level
st.write("### Median Salary by Experience Level")

salary_by_experience_median = Jadarat_df.groupby('سنوات الخبرة')['الراتب بالريال السعودي'].median().reset_index()

# Create a bar chart for median salary
fig_median = px.bar(
    salary_by_experience_median,
    x='سنوات الخبرة',
    y='الراتب بالريال السعودي',
    title="Median Salary by Experience Level",
    labels={'سنوات الخبرة': 'Years of Experience', 'الراتب بالريال السعودي': 'Median Salary (SAR)'},
    color_discrete_sequence=color_theme
)

# Customize layout for clarity
fig_median.update_layout(
    width=800,
    height=500,
    plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
    paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
    font=dict(color='grey'),  # Titles in grey
    xaxis=dict(showline=True, linewidth=1, linecolor='grey'),  # Grey axis lines
    yaxis=dict(showline=True, linewidth=1, linecolor='grey')   # Grey axis lines
)

# Show the median salary chart
st.plotly_chart(fig_median)

# Average Salary by Experience Level
st.write("### Average Salary by Experience Level")

salary_by_experience_mean = Jadarat_df.groupby('سنوات الخبرة')['الراتب بالريال السعودي'].mean().reset_index()

fig_mean = px.bar(
    salary_by_experience_mean,
    x='سنوات الخبرة',
    y='الراتب بالريال السعودي',
    title="Average Salary by Experience Level",
    labels={'سنوات الخبرة': 'Years of Experience', 'الراتب بالريال السعودي': 'Average Salary (SAR)'},
    color_discrete_sequence=color_theme
)

fig_mean.update_layout(
    width=800,
    height=500,
    plot_bgcolor='rgba(0,0,0,0)',  # Transparent background
    paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
    font=dict(color='grey'),  # Titles in grey
    xaxis=dict(showline=True, linewidth=1, linecolor='grey'),  # Grey axis lines
    yaxis=dict(showline=True, linewidth=1, linecolor='grey')   # Grey axis lines
)

st.plotly_chart(fig_mean)

# Salary Range for Fresh Graduates
st.write("### Salary Range for Fresh Graduates")

fresh_graduate_salaries = Jadarat_df[Jadarat_df['سنوات الخبرة'] == 0]['الراتب بالريال السعودي']

if not fresh_graduate_salaries.empty:
    fresh_grad_min = fresh_graduate_salaries.min()
    fresh_grad_max = fresh_graduate_salaries.max()
    fresh_grad_mean = fresh_graduate_salaries.mean()

    st.write(f"The salary range for fresh graduates is between **{fresh_grad_min} SAR** and **{fresh_grad_max} SAR**.")
    st.write(f"The average salary for fresh graduates is **{round(fresh_grad_mean, 2)} SAR**.")
else:
    st.write("No data found for fresh graduates (0 years of experience).")

st.write("""
If you’re a fresh graduate, you’re looking at a **median salary of 4000 SAR**. But here’s where it gets interesting. As you gain experience, your salary will begin to climb. 

After **2 years of experience**, you may experience a slight dip, but once you hit **12 years**, you're looking at salaries that reach **7500 SAR** and beyond. And don’t forget about the average salary — for fresh graduates, it’s around **4676 SAR**. As you build your career, the pay grows with you, and that’s where things get exciting.
""")

st.write("""
So there you have it — a clear picture of what to expect in terms of salaries, job demand, and opportunities in the Saudi job market. Good luck on your job search!
""")
