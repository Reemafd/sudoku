# sudoku
def solve_forward_check(self):
    self.solutions = []


    variables = self.variables[:]
    for variable in variables:
        for value in variable[1][:]:
            for constraint in self.single_constraints:
                if constraint[1] == variable[0]:
                    if not constraint[0](value):
                        variable[1].remove(value)

    first_variable = self._select_next_variable(self.variables[:], self.variable_heuristic)

    self._set_next_node_forward_check([], variables, first_variable)

