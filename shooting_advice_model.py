import feedback_output as feedback_output 
import run_clustering_dbscan as dbscan
import run_decision_tree as decision_tree

def run(level, eye, arrow_locations):
    print(f"Archer level: {level}")
    print(f"Archer eye: {eye}")
    print(f"Arrow locations: {arrow_locations}")

    # Run the clustering model
    clustering_result = dbscan.run(level, eye, arrow_locations)

    # run decision tree model
    decision_tree_result = decision_tree.run(clustering_result)
    equip_prediction = feedback_output.get_equip_feedback(decision_tree_result.equip_results)
    form_prediction = feedback_output.get_form_feedback(decision_tree_result.form_results)

    return [equip_prediction, form_prediction]