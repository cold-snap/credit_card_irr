import numpy_financial as npf

# 参数设置
P = 1.0  # 本金归一化
total_periods = 60
rate_per_period = 0.0019 # 0.142%
prepay_periods = [12, 24, 36, 48, 60]  # 添加60期

# 每期还款额（本金+手续费）
A = P / total_periods + P * rate_per_period

for n in prepay_periods:
    # 构建现金流
    cash_flow = [P]  # 第0期：收到本金
    cash_flow.extend([-A] * (n - 1))  # 前n-1期还款
    
    if n == total_periods:
        # 最后一期正常还款
        cash_flow.append(-A)
    else:
        # 提前还款：当期还款 + 剩余本金
        remaining_principal = P - n * (P / total_periods)
        cash_flow.append(-(A + remaining_principal))
        # 填充剩余期数为0
        cash_flow.extend([0] * (total_periods - n))
    
    # 计算IRR
    monthly_irr = npf.irr(cash_flow)
    annual_irr = (1 + monthly_irr) ** 12 - 1
    
    if n == total_periods:
        print(f"正常还款（{n}期）:")
    else:
        print(f"提前还款（{n}期）:")
    print(f"月IRR: {monthly_irr:.6%}")
    print(f"年化IRR: {annual_irr:.6%}\n")

