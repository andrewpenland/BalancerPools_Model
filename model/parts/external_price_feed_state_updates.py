

def s_update_external_price_feeds(params, substep, state_history, previous_state, policy_input):
    external_prices = policy_input.get('external_price_update')
    if external_prices is None:
        return 'token_prices', previous_state['token_prices']
    return 'token_prices', external_prices

