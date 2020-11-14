def ranking(model_results,ranked_list):
    final_ranking = []
    for i in range(0,len(model_results)):
        if model_results[i]>=0.5:
            final_ranking.append(ranked_list[i])
        else:
            if ranked_list[len(ranked_list)-i-1] not in final_ranking:
                final_ranking.append(ranked_list[len(ranked_list)-i-1])
            else:
                final_ranking.append(ranked_list[i])
    return final_ranking