import duckdb
import load_file_data
import pull_api_data

def main():
    con = duckdb.connect(':memory:')

    load_file_data(con) # TODO - implement this
    pull_api_data(con) # TODO - implement this
    # run_initial_transforms() -- TODO - implement this
    # solve_matrix() -- TODO - implement this
    # run_secondary_transforms() -- TODO - implement this
    # output_results() -- TODO - implement this

if __name__ == "__main__":
    main()