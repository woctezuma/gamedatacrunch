page = str

def test_url_page(number):
    return f'/api/steam/list/all/reviews_total/?page={number}&field=title,release_date,price,base_price_usd,ea_status,review,reviews_total,unfiltered_reviews_total,peak_ccu,followers,playtracker_insight_rank,current_topsellers_rank,reviews_score_fancy,metacritic_score,opencritic_score,hidden_gem_scorel&sort_dir=-1'


