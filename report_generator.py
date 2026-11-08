from fpdf import FPDF
import pandas as pd

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'IPL 19 Seasons Complete Data Analysis (2008-2026)', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def generate_report():
    pdf = PDF()
    pdf.add_page()
    
    try:
        matches = pd.read_csv('matches.csv')
        deliveries = pd.read_csv('deliveries.csv')
        if 'batter' in deliveries.columns:
            deliveries.rename(columns={'batter': 'batsman'}, inplace=True)
        deliveries.replace('NA', np.nan, inplace=True)
        matches.replace('NA', np.nan, inplace=True)
    except:
        pdf.set_font('Arial', '', 12)
        pdf.cell(0, 10, "Data files not found. Please run download_actual_data.py.", 0, 1)
        pdf.output("IPL_Report.pdf")
        return

    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, '1. Executive Summary', 0, 1)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, f"This report covers the analysis of {matches['season'].nunique()} IPL seasons from 2008 to 2026. A total of {matches.shape[0]} matches were played, and {deliveries['total_runs'].sum()} runs were scored in this historic era of T20 cricket.")
    pdf.ln(5)

    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, '2. Team Dominance', 0, 1)
    pdf.set_font('Arial', '', 12)
    wins = matches['winner'].value_counts()
    top_team = wins.index[0]
    top_wins = wins.iloc[0]
    pdf.multi_cell(0, 10, f"The most dominant team over the last 19 seasons has been {top_team} with a staggering {top_wins} match victories.")
    pdf.ln(5)
    
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, '3. The Greatest Players (Top 5)', 0, 1)
    pdf.set_font('Arial', '', 12)
    
    batsman_stats = deliveries.groupby('batsman')['batsman_runs'].sum().reset_index()
    batsman_stats.columns = ['player', 'runs']
    bowler_stats = deliveries.dropna(subset=['player_dismissed'])
    bowler_stats = bowler_stats[bowler_stats['dismissal_kind'] != 'run out']
    wickets = bowler_stats.groupby('bowler').size().reset_index(name='wickets')
    all_players = pd.merge(batsman_stats, wickets, on='player', how='outer').fillna(0)
    all_players['score'] = all_players['runs'] + (all_players['wickets'] * 25)
    top_players = all_players.sort_values('score', ascending=False).head(5)
    
    for i, row in top_players.iterrows():
        pdf.cell(0, 10, f"- {row['player']}: {int(row['runs'])} runs, {int(row['wickets'])} wickets", 0, 1)
    
    pdf.ln(5)

    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, '4. Greatest IPL Team of All Time', 0, 1)
    pdf.set_font('Arial', '', 12)
    team_data = [
        "1. Virat Kohli (Opener)", "2. Chris Gayle (Opener)", "3. Suresh Raina (Top Order)", 
        "4. AB de Villiers (Middle Order)", "5. MS Dhoni (c & wk)", "6. Kieron Pollard (Middle Order)", 
        "7. Andre Russell (All Rounder)", "8. Rashid Khan (Spinner)", "9. Sunil Narine (Spinner)", 
        "10. Lasith Malinga (Fast Bowler)", "11. Jasprit Bumrah (Fast Bowler)"
    ]
    for p in team_data:
        pdf.cell(0, 8, p, 0, 1)
        
    pdf.output("IPL_Report_2008_2026.pdf")
    print("Report generated: IPL_Report_2008_2026.pdf")

if __name__ == "__main__":
    generate_report()
