# DAY 5: LOOPS, ITERATION, AND CONTROL FLOW

## WHAT I BUILT
*   **CURRICULUM MILESTONE PROJECTS:** Completed the foundational loop exercises including the Tasks, FizzBuzz, and the PyPassword Generator.
*   **AI CUSTOM CHALLENGE (THE SELECTIVE NUMBER CRUNCHER):** Built a constraint evaluation loop from 1 to 50 that handles compound mathematical conditions, early loop termination, and explicit default state outputs.

## KEY CONCEPTS LEARNED
*   **DEFENSIVE LOGIC HIERARCHY:** Ordering overlapping conditions (like compound checks) correctly to prevent broader conditions from accidentally hijacking the execution flow.
*   **EXPLICIT STRUCTURAL MAPPING:** Using clear `else` blocks for default application states instead of relying on implicit code fall-through outside the conditional structure.

## ERRORS FACED & SOLVED
*   **VARIABLE MUTATION & EXECUTION FLOW FALL-THROUGH:** Initially placed the compound `break` condition lower down in the `elif` chain and mutated `n = n**2`. Because the `print(n)` statement was sitting completely outside the conditional block, it accidentally processed both the squared numbers and the default numbers. Fixed this by establishing a strict top-down logic order and routing the default state into an explicit `else` block.

## 📝 EXPERIENCE
I decided to strip away the implicit, loose coding habits and focus heavily on structural precision today. On the custom challenge, I successfully caught the hardest part of the logic—ordering the compound condition (`3 and 8`) right at the top so it wouldn't get trapped. 
